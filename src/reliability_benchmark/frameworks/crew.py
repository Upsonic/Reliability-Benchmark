from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel, Field
from typing import Optional, List
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff
import json


from crewai import LLM

# Basic configuration
llm = LLM(model="azure/gpt-4o")

# Response Models


from ..data_class import *

from ..prompts import *


@CrewBase
class ProductDataCrew:
    """Crew for processing and transforming product data from Netsuite"""

    def __init__(self, raw_data: str):
        self.raw_data = raw_data

    @agent
    def general_info_agent(self) -> Agent:
        return Agent(
            role="General Information Specialist",
            goal="Extract general informations from product data",
            backstory="Expert in product general informations",
            llm=llm,
            verbose=True
        )

    @agent
    def product_class_agent(self) -> Agent:
        return Agent(
            role="Product Information Specialist",
            goal="Extract product informations from product data",
            backstory="Expert in product informations",
            llm=llm,
            verbose=True
        )

    @agent
    def spec_agent(self) -> Agent:
        return Agent(
            role="Spec Information Specialist",
            goal="Extract spec informations from product data",
            backstory="Expert in product spec",
            llm=llm,
            verbose=True
        )

    @agent
    def make_agent(self) -> Agent:
        return Agent(
            role="Make Information Specialist",
            goal="Extract Make informations from product data",
            backstory="Expert in product make informations",
            llm=llm,
            verbose=True
        )

    @task
    def process_general_info(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured general information following the GeneralInformations schema",
            agent=self.general_info_agent(),
            output_pydantic=GeneralInformations
        )

    @task
    def process_product_class(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured product classification following the ProductClass schema",
            agent=self.product_class_agent(),
            output_pydantic=ProductClass
        )

    @task
    def process_spec(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured specifications following the Spec schema",
            agent=self.spec_agent(),
            output_pydantic=Spec
        )

    @task
    def process_make(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured manufacturing information following the Make schema",
            agent=self.make_agent(),
            output_pydantic=Make
        )

    # --- NEW AGENT METHODS ---
    @agent
    def shipping_agent(self) -> Agent:
        return Agent(
            role="Shipping Information Specialist",
            goal="Extract shipping informations from product data",
            backstory="Expert in product shipping",
            llm=llm,
            verbose=True
        )

    @agent
    def marketing_agent(self) -> Agent:
        return Agent(
            role="Marketing Information Specialist",
            goal="Extract marketing informations from product data",
            backstory="Expert in product marketing",
            llm=llm,
            verbose=True
        )

    @agent
    def usage_agent(self) -> Agent:
        return Agent(
            role="Usage Information Specialist",
            goal="Extract usage informations from product data",
            backstory="Expert in product usage",
            llm=llm,
            verbose=True
        )

    @agent
    def environmental_agent(self) -> Agent:
        return Agent(
            role="Environmental Information Specialist",
            goal="Extract environmental informations from product data",
            backstory="Expert in product environmental",
            llm=llm,
            verbose=True
        )

    @agent
    def compliance_agent(self) -> Agent:
        return Agent(
            role="Compliance Information Specialist",
            goal="Extract compliance informations from product data",
            backstory="Expert in product compliance",
            llm=llm,
            verbose=True
        )

    # --- NEW TASK METHODS ---
    @task
    def process_shipping(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured shipping information following the Shipping schema",
            agent=self.shipping_agent(),
            output_pydantic=Shipping
        )

    @task
    def process_marketing(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured marketing information following the Marketing schema",
            agent=self.marketing_agent(),
            output_pydantic=Marketing
        )

    @task
    def process_usage(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured usage information following the Usage schema",
            agent=self.usage_agent(),
            output_pydantic=Usage
        )

    @task
    def process_environmental(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured environmental information following the Environmental schema",
            agent=self.environmental_agent(),
            output_pydantic=Environmental
        )

    @task
    def process_compliance(self) -> Task:
        return Task(
            description=f"{main_prompt} {self.raw_data}",
            expected_output="Structured compliance information following the Compliance schema",
            agent=self.compliance_agent(),
            output_pydantic=Compliance
        )

    # --- UPDATED get_crew() ---
    @crew
    def get_crew(self) -> Crew:
        return Crew(
            agents=[
                self.general_info_agent(),
                self.product_class_agent(),
                self.spec_agent(),
                self.make_agent(),
                self.shipping_agent(),
                self.marketing_agent(),
                self.usage_agent(),
                self.environmental_agent(),
                self.compliance_agent(),
            ],
            tasks=[
                self.process_general_info(),
                self.process_product_class(),
                self.process_spec(),
                self.process_make(),
                self.process_shipping(),
                self.process_marketing(),
                self.process_usage(),
                self.process_environmental(),
                self.process_compliance(),
            ],
            process=Process.sequential,
            verbose=True,
            max_rpm=10,
            cache=True
        )

    @before_kickoff
    def prepare_inputs(self, inputs):
        """Prepare the input data before processing"""
        return inputs

    @after_kickoff
    def process_output(self, output):
        """Process the output after crew execution"""
        return output





# --- Ensure any helper functions (like process_product) are defined before __main__ ---
def process_product(product_str: str):
    """Process product data using the crew and return structured output."""
    crew_instance = ProductDataCrew(raw_data=product_str)
    result = crew_instance.get_crew().kickoff()

    # Create structured output with model_dump() to convert Pydantic models to dictionaries
    structured_output = {
        "general_information": result.tasks_output[0].pydantic.model_dump(),
        "spec": result.tasks_output[2].pydantic.model_dump(),
        "product_class": result.tasks_output[1].pydantic.model_dump(),
        "make": result.tasks_output[3].pydantic.model_dump(),
        "shipping": result.tasks_output[4].pydantic.model_dump(),
        "marketing": result.tasks_output[5].pydantic.model_dump(),
        "usage": result.tasks_output[6].pydantic.model_dump(),
        "environmental": result.tasks_output[7].pydantic.model_dump(),
        "compliance": result.tasks_output[8].pydantic.model_dump()
    }
    
    return structured_output

from ..utility import print_completion_stats

def crew_test(product_str):
    result = process_product(product_str)
    print_completion_stats(result)
    return result

if __name__ == "__main__":
    product_str = """
    {
        "netsuite_data":"{\"sku\":\"CVDEP700\",\"name\":\"Airplane Statue\",\"netsuite_internal_id\":\"10633\",\"cv_upc\":\"883581105575\",\"created_at\":\"2019-05-17T08:30:36.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"crestview\",\"website_ids\":[\"1\"],\"price\":37.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":12.4},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":29.66},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":37.95}],\"cv_primary_finish\":\"Blackened\",\"color_family\":\"4141\",\"cv_furniture_weight\":\"5.08\",\"cv_carton_height\":16,\"cv_carton_length\":17,\"cv_carton_width\":13,\"cv_furniture_length\":\"11.75\",\"cv_introdate\":\"2016-04-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"1.44\",\"cv_min_sales_qty\":2,\"short_description\":\"Airplane Statue\",\"cv_furniture_height\":\"6.5\",\"cv_furniture_width\":\"15.75\",\"cv_collection\":\"3884\",\"color\":\"60\",\"cv_carton_weight\":5,\"cv_furniture_volume_cube\":1.44,\"cv_set_of\":\"2938\",\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3778\",\"description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown\\\/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"cv_material\":[\"4041\"],\"cv_style\":[\"4023\"],\"meta_title\":\"Airplane Statue\",\"meta_description\":\"The Crestview Collection Airplane Statue is made with aluminum and has a brown\\\/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"category_ids\":[\"6024\",\"6029\",\"6030\"]}"
    }
    """
    crew_test(product_str)

