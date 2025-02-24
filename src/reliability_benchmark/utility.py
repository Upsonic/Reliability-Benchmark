from typing import Dict, Any, Union, Tuple
from pydantic import BaseModel
import json

def calculate_completion_percentage(data: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    """Calculate the percentage of filled fields in a model instance and return detailed status."""
    total_fields = 0
    filled_fields = 0
    stats = {}
    
    def get_dict_data(obj: Any) -> Dict[str, Any]:
        """Handle both Pydantic models and dictionaries."""
        if hasattr(obj, 'model_dump'):
            return obj.model_dump()
        elif hasattr(obj, 'dict'):
            return obj.dict()
        return obj if isinstance(obj, dict) else {}

    def is_field_filled(value: Any) -> bool:
        """Check if a field has a meaningful value."""
        if value is None:
            return False
        if isinstance(value, (str, list, dict)) and not value:
            return False
        return True

    def process_section(section_data: Dict[str, Any], section_name: str) -> Tuple[int, int, Dict[str, Any]]:
        """Process a section of data and return its statistics."""
        section_total = 0
        section_filled = 0
        fields_status = {}
        
        section_data = get_dict_data(section_data)
        
        for field_name, value in sorted(section_data.items()):
            section_total += 1
            
            if isinstance(value, dict):
                sub_total, sub_filled, sub_status = process_section(value, field_name)
                completion = (sub_filled / sub_total * 100) if sub_total > 0 else 0
                
                fields_status[field_name] = {
                    "is_model": True,
                    "completion": completion,
                    "filled_fields": sub_filled,
                    "total_fields": sub_total,
                    "fields": sub_status
                }
                
                section_total = section_total + sub_total - 1
                section_filled += sub_filled
            else:
                is_filled = is_field_filled(value)
                if is_filled:
                    section_filled += 1
                
                fields_status[field_name] = {
                    "is_model": False,
                    "filled": is_filled,
                    "value": value
                }
        
        return section_total, section_filled, fields_status

    # Process the root data
    data = get_dict_data(data)
    for section_name, section_data in sorted(data.items()):
        if section_data and isinstance(section_data, (dict, BaseModel)):
            section_total, section_filled, fields_status = process_section(section_data, section_name)
            total_fields += section_total
            filled_fields += section_filled
            
            completion = (section_filled / section_total * 100) if section_total > 0 else 0
            stats[section_name] = {
                "is_model": True,
                "completion": completion,
                "filled_fields": section_filled,
                "total_fields": section_total,
                "fields": fields_status
            }
    
    overall_completion = (filled_fields / total_fields * 100) if total_fields > 0 else 0
    return overall_completion, stats

def print_field_status(field_status: Dict[str, Any], indent: int = 0) -> None:
    """Print field status in a hierarchical format."""
    prefix = '  ' * indent
    
    for field_name, status in sorted(field_status.items()):
        if status.get("is_model", False):
            # Print nested model with completion percentage
            completion = status["completion"]
            filled = status["filled_fields"]
            total = status["total_fields"]
            
            symbol = "✓" if completion == 100 else "⚠" if completion > 0 else "✗"
            print(f"{prefix}{symbol} {field_name} ({completion:.1f}% - {filled}/{total} fields):")
            
            # Print nested fields
            print_field_status(status["fields"], indent + 1)
        else:
            # Print individual field
            value = status.get("value")
            is_filled = status.get("filled", False)
            symbol = "✓" if is_filled else "✗"
            
            if is_filled:
                if isinstance(value, (list, tuple)):
                    print(f"{prefix}{symbol} {field_name}: {value}")
                elif isinstance(value, dict):
                    print(f"{prefix}{symbol} {field_name}:")
                    for k, v in sorted(value.items()):
                        print(f"{prefix}    {k}: {v}")
                else:
                    str_value = str(value)
                    if len(str_value) > 50:
                        str_value = str_value[:47] + "..."
                    print(f"{prefix}{symbol} {field_name}: {str_value}")
            else:
                print(f"{prefix}{symbol} {field_name}: Not filled")

def print_completion_stats(data: Union[str, Dict[str, Any], BaseModel]) -> None:
    """
    Print completion statistics for product data.
    
    Args:
        data: Can be a JSON string, dictionary, or Pydantic model
        
    This function provides a detailed breakdown of field completion status,
    showing which fields are filled and their values in a hierarchical format.
    """
    # Handle input data type
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            return
    elif isinstance(data, BaseModel):
        data = data.model_dump()
    elif not isinstance(data, dict):
        print(f"Unsupported data type: {type(data)}")
        return

    # Calculate completion statistics
    overall_completion, stats = calculate_completion_percentage(data)
    
    # Print overall completion
    print(f"\nOverall Product Information Completion: {overall_completion:.1f}%\n")
    print("Detailed Field Status:")
    
    # Print detailed status for each section
    print_field_status(stats)

# Example usage
if __name__ == "__main__":
    example_data = {
        "general_information": {
            "model": "B2061",
            "brand": "Designer Superstar",
            "product_name": "Katha Vase",
            "description": ""
        },
        "spec": {
            "length": 3.0,
            "width": 3.0,
            "height": 7.0,
            "weight": None
        }
    }
    
    print_completion_stats(example_data) 