from typing import List, Optional, Dict, Annotated, Union, Type, TypeVar
from langgraph.graph import Graph, StateGraph, START, END
from langgraph.prebuilt import ToolExecutor
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_openai import AzureChatOpenAI

from ..data_class import *

from ..prompts import *

T = TypeVar('T', bound=BaseModel)

def parse_and_validate_json(content: str, model_class: Type[T], context: str = "") -> T:
    """Helper function to parse and validate JSON responses.
    
    Args:
        content: The response content to parse
        model_class: The Pydantic model class to validate against
        context: Additional context for error messages
        
    Returns:
        Validated model instance
        
    Raises:
        Exception: If parsing or validation fails
    """
    try:
        # Extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        # If there's still no valid JSON, try to find JSON-like structure
        if not content.strip().startswith("{"):
            # Find the first { and last }
            start = content.find("{")
            end = content.rfind("}") + 1
            if start != -1 and end != 0:
                content = content[start:end]
        
        # Validate and return
        return model_class.model_validate_json(content)
    except Exception as e:
        print(f"Error parsing {context}: {e}")
        print(f"Response content: {content}")
        raise

# Initialize the OpenAI chat model
model = AzureChatOpenAI(
    azure_deployment="gpt-4o",
)

# Create structured output models
general_info_model = model.with_structured_output(GeneralInformations,)
product_class_model = model.with_structured_output(ProductClass)
spec_model = model.with_structured_output(Spec)
make_model = model.with_structured_output(Make)
shipping_model = model.with_structured_output(Shipping)
marketing_model = model.with_structured_output(Marketing)
usage_model = model.with_structured_output(Usage)
environmental_model = model.with_structured_output(Environmental)
compliance_model = model.with_structured_output(Compliance)

# Define the state type using Pydantic
class AgentState(BaseModel):
    messages: List[Union[HumanMessage, AIMessage]]
    current_step: str
    general_information: Optional[GeneralInformations] = None
    product_class: Optional[ProductClass] = None
    spec: Optional[Spec] = None
    make: Optional[Make] = None
    shipping: Optional[Shipping] = None
    marketing: Optional[Marketing] = None
    usage: Optional[Usage] = None
    environmental: Optional[Environmental] = None
    compliance: Optional[Compliance] = None

# Define agent functions
def general_info_agent(state: AgentState) -> Dict:
    """Extract general product information"""
    response = general_info_model.invoke(state.messages[0].content)
    return {
        "general_information": response,
        "current_step": "product_class_node"
    }

def product_class_agent(state: AgentState) -> Dict:
    """Extract product classification"""
    response = product_class_model.invoke(state.messages[0].content)
    return {
        "product_class": response,
        "current_step": "spec_node"
    }

def spec_agent(state: AgentState) -> Dict:
    """Extract product specifications"""
    response = spec_model.invoke(state.messages[0].content)
    return {
        "spec": response,
        "current_step": "make_node"
    }

def make_agent(state: AgentState) -> Dict:
    """Extract manufacturing details"""
    response = make_model.invoke(state.messages[0].content)
    return {
        "make": response,
        "current_step": "shipping_node"
    }

def shipping_agent(state: AgentState) -> Dict:
    """Extract shipping information"""
    response = shipping_model.invoke(state.messages[0].content)
    return {
        "shipping": response,
        "current_step": "marketing_node"
    }

def marketing_agent(state: AgentState) -> Dict:
    """Extract marketing information"""
    response = marketing_model.invoke(state.messages[0].content)
    return {
        "marketing": response,
        "current_step": "usage_node"
    }

def usage_agent(state: AgentState) -> Dict:
    """Extract usage information"""
    response = usage_model.invoke(state.messages[0].content)
    return {
        "usage": response,
        "current_step": "environmental_node"
    }

def environmental_agent(state: AgentState) -> Dict:
    """Extract environmental information"""
    response = environmental_model.invoke(state.messages[0].content)
    return {
        "environmental": response,
        "current_step": "compliance_node"
    }

def compliance_agent(state: AgentState) -> Dict:
    """Extract compliance information"""
    response = compliance_model.invoke(state.messages[0].content)
    return {
        "compliance": response,
        "current_step": "end"
    }

# Define the workflow graph
workflow = StateGraph(AgentState)

# Add nodes for each agent
workflow.add_node("general_info_node", general_info_agent)
workflow.add_node("product_class_node", product_class_agent)
workflow.add_node("spec_node", spec_agent)
workflow.add_node("make_node", make_agent)
workflow.add_node("shipping_node", shipping_agent)
workflow.add_node("marketing_node", marketing_agent)
workflow.add_node("usage_node", usage_agent)
workflow.add_node("environmental_node", environmental_agent)
workflow.add_node("compliance_node", compliance_agent)

# Define edges
workflow.add_edge(START, "general_info_node")
workflow.add_edge("general_info_node", "product_class_node")
workflow.add_edge("product_class_node", "spec_node")
workflow.add_edge("spec_node", "make_node")
workflow.add_edge("make_node", "shipping_node")
workflow.add_edge("shipping_node", "marketing_node")
workflow.add_edge("marketing_node", "usage_node")
workflow.add_edge("usage_node", "environmental_node")
workflow.add_edge("environmental_node", "compliance_node")
workflow.add_edge("compliance_node", END)

# Compile the graph
graph = workflow.compile()

def process_product(product_str: str) -> Product:
    """Process product data using LangGraph workflow"""
    
    # Initialize the state
    initial_state = AgentState(
        messages=[HumanMessage(content=product_str)],
        current_step="general_info_node"
    )
    
    # Run the graph
    final_state = graph.invoke(initial_state)
    
    # Combine all components into Product
    product = Product(
        general_information=final_state["general_information"],
        product_class=final_state["product_class"],
        spec=final_state["spec"],
        make=final_state["make"],
        shipping=final_state["shipping"],
        marketing=final_state["marketing"],
        usage=final_state["usage"],
        environmental=final_state["environmental"],
        compliance=final_state["compliance"]
    )
    
    return product


from ..utility import print_completion_stats

def lang_test(product_str):
    product = process_product(product_str)
    product_data = product.model_dump()
    print_completion_stats(product_data)
    return product_data

# Example usage
if __name__ == "__main__":
    product_str = main_prompt + """
    {
        "netsuite_data":"{\"sku\":\"CVDEP700\",\"name\":\"Airplane Statue\",\"netsuite_internal_id\":\"10633\",\"cv_upc\":\"883581105575\",\"created_at\":\"2019-05-17T08:30:36.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"crestview\",\"website_ids\":[\"1\"],\"price\":37.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":12.4},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":29.66},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":37.95}],\"cv_primary_finish\":\"Blackened\",\"color_family\":\"4141\",\"cv_furniture_weight\":\"5.08\",\"cv_carton_height\":16,\"cv_carton_length\":17,\"cv_carton_width\":13,\"cv_furniture_length\":\"11.75\",\"cv_introdate\":\"2016-04-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"1.44\",\"cv_min_sales_qty\":2,\"short_description\":\"Airplane Statue\",\"cv_furniture_height\":\"6.5\",\"cv_furniture_width\":\"15.75\",\"cv_collection\":\"3884\",\"color\":\"60\",\"cv_carton_weight\":5,\"cv_furniture_volume_cube\":1.44,\"cv_set_of\":\"2938\",\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3778\",\"description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"cv_material\":[\"4041\"],\"cv_style\":[\"4023\"],\"meta_title\":\"Airplane Statue\",\"meta_description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"category_ids\":[\"6024\",\"6029\",\"6030\"]}"
    }
    """
    
    lang_test(product_str) 