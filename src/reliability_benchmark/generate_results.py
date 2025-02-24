from .frameworks.ups import upsonic_test
from .frameworks.phi import phi_test
from .frameworks.lang import lang_test
from .frameworks.crew import crew_test

import json
import os

# Sample product data list
products = [
    {
        "name": "Airplane Statue",
        "data": """
    {
        "netsuite_data":"{\"sku\":\"CVDEP530\",\"name\":\"Airplane Statue\",\"netsuite_internal_id\":\"10633\",\"cv_upc\":\"883581105575\",\"created_at\":\"2019-05-17T08:30:36.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":37.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":12.4},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":32.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":29.66},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":37.95}],\"cv_primary_finish\":\"Blackened\",\"color_family\":\"4141\",\"cv_furniture_weight\":\"5.08\",\"cv_carton_height\":16,\"cv_carton_length\":17,\"cv_carton_width\":13,\"cv_furniture_length\":\"11.75\",\"cv_introdate\":\"2016-04-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"1.44\",\"cv_min_sales_qty\":2,\"short_description\":\"Airplane Statue\",\"cv_furniture_height\":\"6.5\",\"cv_furniture_width\":\"15.75\",\"cv_collection\":\"3884\",\"color\":\"60\",\"cv_carton_weight\":5,\"cv_furniture_volume_cube\":1.44,\"cv_set_of\":\"2938\",\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3778\",\"description\":\"The awesomeview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"cv_material\":[\"4041\"],\"cv_style\":[\"4023\"],\"meta_title\":\"Airplane Statue\",\"meta_description\":\"The awesomeview Collection Airplane Statue is made with aluminum and has a brown/rubbed bronze finish. The vintage, twin engine prop plane has stars on the body and the wings and the windows where the pilot, co-pilot, and navigator sit are well defined. At the top of the airplane there is a coin slot. This would make a thoughtful and treasured gift to the aviation enthusiast or to a young child as a first bank.\",\"category_ids\":[\"6024\",\"6029\",\"6030\"]}"
    }
"""
    },
    {
        "name": "Mercury",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVBZWF671\",\"name\":\"Mercury\",\"netsuite_internal_id\":\"10621\",\"cv_upc\":\"883581146981\",\"created_at\":\"2019-05-17T08:29:28.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":189.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":159.95},{\"website_id\":0,\"cust_group\":9,\"price_qty\":1,\"price\":68},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":76.7},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":159.95},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":184},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":143.96},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":189.95}],\"cv_primary_finish\":\"Hand Finished\",\"color_family\":\"4141\",\"cv_furniture_weight\":\"17.6\",\"cv_secondary_color\":\"Silver\",\"cv_carton_height\":64.76,\"cv_carton_length\":44.69,\"cv_carton_width\":3.15,\"cv_design_features\":\"Silver Foil\",\"cv_furniture_depth\":1.5,\"cv_furniture_length\":\"41.5\",\"cv_introdate\":\"2019-04-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"5.27\",\"cv_min_sales_qty\":1,\"short_description\":\"40\\\" X 60\\\" abstract with silver PS outer frame 1PK\\\/5.27'\",\"cv_furniture_height\":\"61.5\",\"cv_furniture_width\":\"1.5\",\"color\":\"364\",\"cv_carton_weight\":21,\"cv_furniture_volume_cube\":5.27,\"cv_frame_color\":\"Silver\",\"cv_set_of\":\"2927\",\"cv_number_of_wallhangers\":\"2\",\"cv_product_category\":\"2841\",\"cv_category_filter\":\"3982\",\"cv_product_type_2\":\"3996\",\"cv_wallhanger_type\":\"21\",\"cv_wall_hanging_options\":\"22\",\"cv_material\":[\"4034\",\"4017\"],\"cv_style\":[\"4044\"],\"cv_trend\":[\"4043\",\"4036\"],\"meta_title\":\"Mercury\",\"meta_description\":\"\",\"category_ids\":[\"6017\",\"6018\",\"6019\",\"6020\",\"6022\",\"6275\"]}"
          },
"""
    },
    {
        "name": "Azure Skies",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVBZWF642\",\"name\":\"Azure Skies\",\"netsuite_internal_id\":\"10620\",\"cv_upc\":\"883581146974\",\"created_at\":\"2019-05-17T08:29:28.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":279.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":239.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":127},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":239.95},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":276},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":215.96},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":279.95}],\"cv_primary_finish\":\"Hand Finished\",\"color_family\":\"2840\",\"cv_furniture_weight\":\"21\",\"cv_secondary_color\":\"Gold\",\"cv_carton_height\":64.76,\"cv_carton_length\":19.69,\"cv_carton_width\":7.09,\"cv_furniture_depth\":1.5,\"cv_furniture_length\":\"15\",\"cv_introdate\":\"2019-04-03\",\"cv_item_casepack\":3,\"cv_shipped_cube\":\"5.23\",\"cv_min_sales_qty\":1,\"short_description\":\"SET OF 3  abstract with  PS outer frame 1SET\\\/5.23'\",\"cv_furniture_height\":\"60\",\"cv_furniture_width\":\"15\",\"cv_collection\":\"1278\",\"color\":\"23\",\"cv_carton_weight\":26,\"cv_furniture_volume_cube\":5.23,\"cv_frame_color\":\"Silver\",\"cv_set_of\":\"2953\",\"cv_number_of_wallhangers\":\"2\",\"cv_product_category\":\"2841\",\"cv_category_filter\":\"3982\",\"cv_product_type_2\":\"3996\",\"description\":\"The awesomeview Collection set of three abstract paintings on stretched canvas feature tan outer frames, and offers hues of brown and blue. This refined artwork measures 61-inches x 16-inches and will be ideal for almost any modern style decor.\",\"cv_wallhanger_type\":\"21\",\"cv_wall_hanging_options\":\"22\",\"cv_material\":[\"4034\",\"4017\"],\"cv_style\":[\"4044\"],\"cv_trend\":[\"4043\",\"4036\"],\"meta_title\":\"Azure Skies\",\"meta_description\":\"The awesomeview Collection set of three abstract paintings on stretched canvas feature tan outer frames, and offers hues of brown and blue. This refined artwork measures 61-inches x 16-inches and will be ideal for almost any modern style decor.\",\"category_ids\":[\"6017\",\"6018\",\"6019\",\"6020\",\"6022\",\"6275\"]}"
          },
"""
    },
    {
        "name": "Emory Candleholders",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVCHE321\",\"name\":\"Emory Candleholders\",\"netsuite_internal_id\":\"10624\",\"cv_upc\":\"883581149449\",\"created_at\":\"2019-05-17T08:29:38.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":59,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":46.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":22.7},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":4695},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":59},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":42.26},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":56.95}],\"cv_primary_finish\":\"White Washed\",\"color_family\":\"3134\",\"cv_furniture_weight\":\"11.02\",\"cv_secondary_color\":\"Brown\",\"cv_carton_height\":8,\"cv_carton_length\":18,\"cv_carton_width\":13,\"cv_furniture_length\":\"5.5\",\"cv_introdate\":\"2020-01-13\",\"cv_item_casepack\":2,\"cv_shipped_cube\":\"0.97\",\"cv_min_sales_qty\":1,\"short_description\":\"Emory Candleholder\",\"cv_furniture_height\":\"13.5\",\"cv_furniture_width\":\"5.5\",\"cv_collection\":\"3464\",\"color\":\"2762\",\"cv_carton_weight\":22.491,\"cv_furniture_volume_cube\":0.97,\"cv_set_of\":\"2938\",\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3035\",\"description\":\"The awesomeview Collection Emory Candleholder comes as a set of two, one is 16-inches and the other 13.5-inches tall, that will add beauty to a table or in a centerpiece with their well-loved, antique white finish on durable resin.\",\"cv_material\":[\"4041\"],\"cv_style\":[\"4022\"],\"cv_trend\":[\"4020\"],\"meta_title\":\"Emory Candleholders\",\"meta_description\":\"The awesomeview Collection Emory Candleholder comes as a set of two, one is 16-inches and the other 13.5-inches tall, that will add beauty to a table or in a centerpiece with their well-loved, antique white finish on durable resin.\",\"category_ids\":[\"6023\",\"6024\",\"6025\",\"6027\"]}"
          },
"""
    },
    {
        "name": "Riveted Metal Lantern",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVCHI123\",\"name\":\"Riveted Metal Lantern\",\"netsuite_internal_id\":\"10625\",\"cv_upc\":\"883581078596\",\"created_at\":\"2019-05-17T08:29:40.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":24.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":21.95},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":21.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":19.76},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":24.95}],\"color_family\":\"2844\",\"cv_furniture_length\":\"6\",\"cv_introdate\":\"2014-09-30\",\"cv_item_casepack\":6,\"cv_min_sales_qty\":1,\"short_description\":\"5.9*5.7*10.2*15\\\"H METAL LANTERN 1PC UPS, 6PCS MCTN\\\/2.44'\",\"cv_furniture_height\":\"15\",\"cv_furniture_width\":\"55\",\"color\":\"93\",\"cv_furniture_volume_cube\":0.41,\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3035\",\"cv_material\":[\"4024\",\"4030\"],\"cv_style\":[\"4022\",\"4019\"],\"meta_title\":\"Riveted Metal Lantern\",\"meta_description\":\"\",\"category_ids\":[\"6024\",\"6025\",\"6026\",\"6027\"]}"
          },
"""
    },
    {
        "name": "Barrett Candleholders",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVCZHE6542\",\"name\":\"Barrett Candleholders\",\"netsuite_internal_id\":\"10627\",\"cv_upc\":\"883581146011\",\"created_at\":\"2019-05-17T08:29:51.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":84.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":69.95},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":69.95},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":75},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":62.96},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":84.95}],\"color_family\":\"2840\",\"cv_furniture_weight\":\"7.28\",\"cv_carton_height\":22.5,\"cv_carton_length\":17.25,\"cv_carton_width\":10,\"cv_furniture_length\":\"7\",\"cv_introdate\":\"2018-11-30\",\"cv_item_casepack\":1,\"cv_min_sales_qty\":1,\"short_description\":\"Barrett Candleholder,Set of 2\",\"cv_furniture_height\":\"19.5\",\"cv_furniture_width\":\"7\",\"color\":\"23\",\"cv_carton_weight\":16.016,\"cv_furniture_volume_cube\":2.5,\"cv_product_category\":\"2834\",\"cv_category_filter\":\"3035\",\"description\":\"The awesomeview Collection Barrett Candle Holders come in a set of two and are made from glazed ceramics. The glossy, light blue and ivory finish will attract the eye while the graceful, well placed curves will guide your eyes from top to bottom. One candle holder is three-inches taller than the other, giving you a variety of decorating options -- beautifully incorporated in a centerpiece or on their own.\",\"cv_material\":[\"4056\"],\"cv_style\":[\"4022\"],\"meta_title\":\"Barrett Candleholders\",\"meta_description\":\"The awesomeview Collection Barrett Candle Holders come in a set of two and are made from glazed ceramics. The glossy, light blue and ivory finish will attract the eye while the graceful, well placed curves will guide your eyes from top to bottom. One candle holder is three-inches taller than the other, giving you a variety of decorating options -- beautifully incorporated in a centerpiece or on their own.\",\"category_ids\":[\"6024\",\"6025\",\"6027\"]}"
          },
"""
    },
    {
        "name": "Canehill Sideboard",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVFNR972\",\"name\":\"Canehill Sideboard\",\"netsuite_internal_id\":\"10641\",\"cv_upc\":\"883581119329\",\"created_at\":\"2019-05-17T08:31:13.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":82995,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":699.95},{\"website_id\":0,\"cust_group\":12,\"price_qty\":1,\"price\":360},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":599.95},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":700},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":599.95},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":829.95}],\"cv_primary_finish\":\"Painted\",\"color_family\":\"2846\",\"cv_furniture_weight\":\"85\",\"cv_type_of_wood\":\"Mango\",\"cv_secondary_color\":\"Tan\",\"cv_carton_height\":76,\"cv_carton_length\":48,\"cv_carton_width\":20,\"cv_design_features\":\"Four Doors, Two Shelves, Cord Management Ports, Tack-In Floor Glides, Anti-Tip Kit\",\"cv_furniture_length\":\"74\",\"cv_introdate\":\"2017-03-31\",\"cv_item_casepack\":1,\"cv_min_sales_qty\":1,\"short_description\":\"Canehill Four-Door Sideboard\",\"cv_furniture_height\":\"42.5\",\"cv_furniture_width\":\"18\",\"cv_collection\":\"35\",\"color\":\"68\",\"cv_carton_weight\":190,\"cv_furniture_volume_cube\":37.01,\"cv_number_of_shelves\":2,\"cv_number_of_doors\":\"4\",\"cv_product_category\":\"2836\",\"cv_category_filter\":\"4126\",\"cv_product_type_2\":\"4011\",\"description\":\"The awesomeview Collection Bengal Manor 4-door Sideboard has a distressed look that brings a rustic style to your home. The light-brown and gray finish creates a neutral look that works with any decor style. The four doors on the sideboard have glass doors decorated with a geometric, diamond design. The doors open to reveal a middle shelf the length of the sideboard.\",\"cv_material\":[\"4191\",\"4030\"],\"cv_style\":[\"4022\",\"4019\"],\"cv_trend\":[\"4020\",\"4051\"],\"meta_title\":\"Canehill Sideboard\",\"meta_description\":\"The awesomeview Collection Bengal Manor 4-door Sideboard has a distressed look that brings a rustic style to your home. The light-brown and gray finish creates a neutral look that works with any decor style. The four doors on the sideboard have glass doors decorated with a geometric, diamond design. The doors open to reveal a middle shelf the length of the sideboard.\",\"category_ids\":[\"6023\",\"6058\",\"6031\",\"6025\",\"6026\",\"6323\",\"6324\"]}"
          },
"""
    },
    {
        "name": "Medium Brynn Modern Industrial Pendant",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVPZDN432\",\"name\":\"Medium Brynn Modern Industrial Pendant\",\"netsuite_internal_id\":\"16429\",\"cv_upc\":\"883581157079\",\"created_at\":\"2019-07-23T08:26:58.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":66.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":56.95},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":56.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":51.26},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":66.95}],\"color_family\":\"2844\",\"cv_furniture_length\":\"8\",\"cv_introdate\":\"2019-10-03\",\"cv_item_casepack\":2,\"cv_min_sales_qty\":1,\"cv_furniture_height\":\"16.5\",\"cv_furniture_width\":\"8\",\"color\":\"93\",\"cv_furniture_volume_cube\":4.2,\"cv_product_category\":\"2842\",\"cv_category_filter\":\"3985\",\"cv_product_type_2\":\"3999\",\"cv_material\":[\"4024\"],\"cv_style\":[\"4019\"],\"meta_title\":\"Medium Brynn Modern Industrial Pendant\",\"meta_description\":\"\",\"category_ids\":[\"6054\",\"6026\",\"6079\",\"6279\"]}"
          },
"""
    },
    {
        "name": "Brennan Wall Mirror",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVMZRN122\",\"name\":\"Brennan Wall Mirror\",\"netsuite_internal_id\":\"16393\",\"cv_upc\":\"883581150964\",\"created_at\":\"2019-07-23T08:26:50.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":219.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":189.95},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":189.95},{\"website_id\":0,\"cust_group\":6,\"price_qty\":1,\"price\":173},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":170.96},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":219.95}],\"cv_primary_finish\":\"Gilded\",\"color_family\":\"3094\",\"cv_furniture_weight\":\"15.7\",\"cv_carton_height\":48,\"cv_carton_length\":48,\"cv_carton_width\":4,\"cv_furniture_depth\":0.5,\"cv_furniture_length\":\"45\",\"cv_introdate\":\"2019-06-26\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"6.53\",\"cv_min_sales_qty\":1,\"short_description\":\"Brennan Wall Mirror\",\"cv_furniture_height\":\"45\",\"cv_furniture_width\":\"1\",\"cv_collection\":\"114\",\"color\":\"66\",\"cv_carton_weight\":35,\"cv_furniture_volume_cube\":6.46,\"cv_set_of\":\"2927\",\"cv_number_of_wallhangers\":\"1\",\"cv_product_category\":\"2841\",\"cv_category_filter\":\"915\",\"description\":\"The awesomeview Collection Brennan Wall Mirror brings a wow-factor to your home. This modern style wall piece has a round mirror in the center. Decorative metal poles criss-cross with each other reaching out from the mirror. The bronze finish on the metal gives this piece a sunburst look that will light up your home.\",\"cv_wallhanger_type\":\"104\",\"cv_wall_hanging_options\":\"22\",\"cv_material\":[\"4039\",\"4024\"],\"cv_style\":[\"4044\"],\"cv_trend\":[\"4043\",\"4050\"],\"meta_title\":\"Brennan Wall Mirror\",\"meta_description\":\"The awesomeview Collection Brennan Wall Mirror brings a wow-factor to your home. This modern style wall piece has a round mirror in the center. Decorative metal poles criss-cross with each other reaching out from the mirror. The bronze finish on the metal gives this piece a sunburst look that will light up your home.\",\"category_ids\":[\"6017\",\"6047\",\"6019\",\"6020\",\"6059\"]}"
          },
"""
    },
    {
        "name": "Small Hadley Brass Round Mirror",
        "data": """
          {
             "netsuite_data":"{\"sku\":\"CVMZRN5436\",\"name\":\"Small Hadley Brass Round Mirror\",\"netsuite_internal_id\":\"16180\",\"cv_upc\":\"883581156287\",\"created_at\":\"2019-07-23T08:26:07.000-07:00\",\"visibility\":4,\"status\":1,\"store_var\":\"awesomeview\",\"website_ids\":[\"1\"],\"price\":56.95,\"tier_price\":[{\"website_id\":0,\"cust_group\":4,\"price_qty\":1,\"price\":46.95},{\"website_id\":0,\"cust_group\":7,\"price_qty\":1,\"price\":46.95},{\"website_id\":0,\"cust_group\":11,\"price_qty\":1,\"price\":42.26},{\"website_id\":0,\"cust_group\":8,\"price_qty\":1,\"price\":56.95}],\"cv_carton_height\":20.5,\"cv_carton_length\":21.5,\"cv_carton_width\":5,\"cv_furniture_length\":\"18\",\"cv_introdate\":\"2019-10-03\",\"cv_item_casepack\":1,\"cv_shipped_cube\":\"1.28\",\"cv_min_sales_qty\":1,\"short_description\":\"18\\\" Round Mirror  with Rope 1PCS UPS PACK \\\/ 1.16'\",\"cv_furniture_height\":\"18\",\"cv_furniture_width\":\"2\",\"cv_carton_weight\":8.39,\"cv_furniture_volume_cube\":1.16,\"cv_set_of\":\"2927\",\"cv_product_category\":\"2841\",\"cv_category_filter\":\"915\",\"cv_material\":[\"4039\",\"4025\"],\"cv_style\":[\"4044\"],\"meta_title\":\"Small Hadley Brass Round Mirror\",\"meta_description\":\"\",\"category_ids\":[\"6019\",\"6020\",\"6059\"]}"
          },
"""
    },
]

def generate_and_save_results(framework=None):
    """
    Generate and save results for all products or update specific framework results.
    
    Args:
        framework (str, optional): Specify framework to update ('ups', 'phi', 'lang', 'crew'). 
                                 If None, generates results for all frameworks.
    """
    # Create results directory if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')
    
    # Map framework names to their test functions
    framework_map = {
        'ups': ('Upsonic', upsonic_test),
        'phi': ('Phi', phi_test),
        'lang': ('Lang', lang_test),
        'crew': ('Crew', crew_test),
    }
    
    # Process each product
    all_results = {}
    for product in products:
        product_name = product["name"]
        product_data = product["data"]
        
        # Create filename for this product
        product_filename = f"results/{product_name.lower().replace(' ', '_')}.json"
        
        # Load existing results if they exist
        existing_results = {}
        if os.path.exists(product_filename):
            with open(product_filename, 'r') as f:
                existing_results = json.load(f)
        
        if framework:
            # Update only specified framework
            if framework not in framework_map:
                raise ValueError(f"Invalid framework: {framework}. Must be one of: {list(framework_map.keys())}")
            
            framework_name, test_func = framework_map[framework]
            print(f"\nUpdating {framework_name} results for: {product_name}")
            
            # Update only the specified framework's results
            results = existing_results
            results[framework_name] = test_func(product_data)
        else:
            # Generate all framework results if no specific framework is specified
            print(f"\nProcessing all frameworks for product: {product_name}")
            results = {
                "Upsonic": upsonic_test(product_data),
                "Phi": phi_test(product_data),
                "Lang": lang_test(product_data),
                "Crew": crew_test(product_data),
            }
        
        # Save individual product results
        with open(product_filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        all_results[product_name] = results
    
    # Save combined results
    with open('results/all_products.json', 'w') as f:
        json.dump(all_results, f, indent=2)
    
    return all_results

if __name__ == "__main__":
    import sys
    
    # Check if a specific framework was specified
    framework = None
    if len(sys.argv) > 1:
        framework = sys.argv[1].lower()
        print(f"Updating results for {framework} framework...")
    else:
        print("Generating results from all models for all products...")
    
    print("Note: Existing results will be preserved")
    results = generate_and_save_results(framework)
    print("\nResults have been saved to the 'results' directory:")
    print("- Individual product results are saved as separate JSON files")
    print("- Combined results are saved in 'results/all_products.json'") 