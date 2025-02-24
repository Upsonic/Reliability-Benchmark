from upsonic import Agent, Task, ObjectResponse
from pydantic import BaseModel, Field
from typing import Optional
from dataclasses import fields
import json

# Creating Agent
class ReliabilityLayer:
    prevent_hallucination = 10

agent = Agent("Data Transformator AI", debug=True, model="azure/gpt-4o", reliability_layer=ReliabilityLayer, compress_context=False, sub_task=False)

# Response Types

from ..data_class import *

from ..prompts import *

# Separate tasks for each component
def process_general_info(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=GeneralInformations_upsonic)

def process_product_class(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=ProductClass_upsonic)

def process_spec(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Spec_upsonic)

def process_make(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Make_upsonic)

def process_shipping(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Shipping_upsonic)

def process_marketing(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Marketing_upsonic)

def process_usage(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Usage_upsonic)

def process_environmental(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Environmental_upsonic)

def process_compliance(raw_data: str) -> Task:
    return Task(main_prompt + raw_data, response_format=Compliance_upsonic)







def upsonic_agent(product_str: str) -> Product:
    # Process each component
    general_info = agent.do(process_general_info(product_str))
    product_class = agent.do(process_product_class(product_str))
    spec = agent.do(process_spec(product_str))
    make = agent.do(process_make(product_str))
    shipping = agent.do(process_shipping(product_str))
    marketing = agent.do(process_marketing(product_str))
    usage = agent.do(process_usage(product_str))
    environmental = agent.do(process_environmental(product_str))
    compliance = agent.do(process_compliance(product_str))

    # Combine all components into Product
    product = Product_upsonic(
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


def upsonic_test(product_str):
    the_product = upsonic_agent(product_str)
    # Print completion stats
    product_data = the_product.model_dump()
    print_completion_stats(product_data)
    return product_data

