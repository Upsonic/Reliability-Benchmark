from typing import List, Optional
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.azure import AzureOpenAI


from ..data_class import *

from ..prompts import *

from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI chat model

chat = AzureOpenAI(
    id="gpt-4o",
)

# Create agents for each component
general_info_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=GeneralInformations,
    structured_outputs=True,
)

product_class_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=ProductClass,
    structured_outputs=True,
)

spec_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Spec,
    structured_outputs=True,
)

make_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Make,
    structured_outputs=True,
)

shipping_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Shipping,
    structured_outputs=True,
)

marketing_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Marketing,
    structured_outputs=True,
)

usage_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Usage,
    structured_outputs=True,
)

environmental_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Environmental,
    structured_outputs=True,
)

compliance_agent = Agent(
    model=chat,
    description=main_prompt,
    response_model=Compliance,
    structured_outputs=True,
)

def process_product(product_str: str) -> Product:
    """Process product data using multiple specialized agents"""
    
    # Get responses from each agent and extract content
    general_info = general_info_agent.run(product_str).content
    product_class = product_class_agent.run(product_str).content
    spec = spec_agent.run(product_str).content
    make = make_agent.run(product_str).content
    shipping = shipping_agent.run(product_str).content
    marketing = marketing_agent.run(product_str).content
    usage = usage_agent.run(product_str).content
    environmental = environmental_agent.run(product_str).content
    compliance = compliance_agent.run(product_str).content

    # Combine all components into Product
    product = Product(
        general_information=general_info,
        spec=spec,
        product_class=product_class,
        make=make,
        shipping=shipping,
        marketing=marketing,
        usage=usage,
        environmental=environmental,
        compliance=compliance
    )
    
    return product


from ..utility import print_completion_stats

def phi_test(product_str):
    product = process_product(product_str)
    product_data = product.model_dump()
    print_completion_stats(product_data)
    return product_data

# Example usage
if __name__ == "__main__":
    product_str = """
    {
        "netsuite_data":"{\"sku\":\"CVDEP700\",\"name\":\"Airplane Statue\",\"netsuite_internal_id\":\"10633\",\"cv_upc\":\"883581105575\",\"created_at\":\"2019-05-17T08:30:36.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"crestview\",\"website_ids\":[\"1\"],\"price\":37.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":12.4},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":29.66},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":37.95}],\"cv_primary_finish\":\"Blackened\",\"color_family\":\"4141\",\"cv_furniture_weight\":\"5.08\",\"cv_carton_height\":16,\"cv_carton_length\":17,\"cv_carton_width\":13,\"cv_furniture_length\":\"11.75\",\"cv_introdate\":\"2016-04-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"1.44\",\"cv_min_sales_qty\":2,\"short_description\":\"Airplane Statue\",\"cv_furniture_height\":\"6.5\",\"cv_furniture_width\":\"15.75\",\"cv_collection\":\"3884\",\"color\":\"60\",\"cv_carton_weight\":5,\"cv_furniture_volume_cube\":1.44,\"cv_set_of\":\"2938\",\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3778\",\"description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"cv_material\":[\"4041\"],\"cv_style\":[\"4023\"],\"meta_title\":\"Airplane Statue\",\"meta_description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"category_ids\":[\"6024\",\"6029\",\"6030\"]}"
    }
    """
    
    phi_test(product_str) 