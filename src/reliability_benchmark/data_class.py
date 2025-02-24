from typing import List, Optional
from pydantic import BaseModel, Field



# Response Models
class GeneralInformations(BaseModel):
    model: str = Field(description="Manufacturer model number. Ex: B2061")
    brand: str = Field(description="Item brand. Ex: Designer Superstar")
    upc: int = Field(description="UPC code, 12 digits. Ex: 043000181706")
    asin: str = Field(description="ASIN code, 10 chars. Ex: B08Z5NYG12")
    product_name: str = Field(description="Product name. Ex: Katha Vase")
    specifier: str = Field(description="Product name specifier. Ex: Coper, Small")
    fullName: str = Field(description="Full product name. Ex: Katha Vase, Coper, Small (dia 3x7'h)")
    description: str = Field(description="Short item description")
    product_class: str = Field(description="Product class based on standard classification")
    origin: str = Field(description="Country of origin, ISO3 country code (3 chars). Ex: USA")

class ProductClass(BaseModel):
    category: list[str] = Field(description="Marketing categories the product belongs to (comma separated values). Ex: ['Vases', 'Outdoor', 'Accents']")
    collection: list[str] = Field(description="List of collections item belongs to (comma separated values). Ex: ['Modern Chic', 'Timeless']")
    style: list[str] = Field(description="List of styles (comma separated values). Ex: ['Minimal', 'Modern']")

class Spec(BaseModel):
    length: float = Field(description="Item overall length expressed in units defined in core.units (number). Ex: 3")
    width: float = Field(description="Item overall width expressed in units defined in core.units (number). Ex: 3")
    height: float = Field(description="Item overall height expressed in units defined in core.units (number). Ex: 7")
    weight: float = Field(description="Item overall weight expressed in units defined in core.units (number). Ex: 1.5")
    dominantColor: list[str]= Field(description="Item main colors, see def.colors for options (comma separated). Ex: ['orangered', 'black']")
    dominantColorFamily: list[str]= Field(description="Main color family, standardized 16 color palette (comma separated). Ex: ['orange', 'black']")
    dominantColorTerm: list[str]= Field(description="Marketing color term (comma separated). Ex: ['siena orange', 'obsidian']")
    dominantColorSaturation: str = Field(description="Choice of vibrant, normal, desaturated")
    secondaryColor: list[str]= Field(description="Item secondary colors, see def.colors for options (comma separated)")
    secondaryColorFamily: list[str]= Field(description="Secondary color family, standardized 16 color palette (comma separated)")
    secondaryColorTerm: list[str]= Field(description="Marketing color term (comma separated)")
    patternType: list[str]= Field(description="Choice of solid, quilted, pattern")
    motiff: str = Field(description="Pattern motif if applicable. Ex: Faux leather")

class Make(BaseModel):
    primaryMaterials: list[str]= Field(description="Primary material family (choice of steel, aluminum, glass, fabric, iron, brass). Ex: ['wood', 'metal']")
    primaryMaterialDetails: str = Field(description="Primary material details (string, comma separated). Ex: 'Accacia wood, stainless steel'")
    additionalMaterials: list[str]= Field(description="Additional materials family (string, comma separated, options tbd)")
    additionalMaterialsDetails: str = Field(description="Additional materials description (string, comma separated, options tbd)")
    containsTextile: str = Field(description="Contains textile materials (choice of YES, NO)")
    textileMaterial: list[str]= Field(description="Textile material family (choice of Sateen, Lyocel, Bamboo, Microfiber, Linen, Flannel, Blend, Polyester, Cotton, Cotton Blend, Wool, Merino Wool). Ex: ['wool', 'lycra']")
    textileComposition: str = Field(description="Description of the textile composition. Ex: '80% wool, 20% elastane'")
    threadCount: str = Field(description="Thread count for textile material if applicable")
    finishFamily: str = Field(description="General finish family if applicable (string, options tbd). Ex: 'bronze'")
    finishDetails: str = Field(description="Finish descriptions. Ex: 'brushed bronze'")

class Shipping(BaseModel):
    method: str = Field(description="Default shipping method (if ships alone) (choice of LTL, PARCEL). Ex: 'PARCEL'")
    oversized: str = Field(description="Package is oversized for shipping method (choice of YES, NO). Ex: 'NO'")
    class_: str = Field(description="Freight class (optional)")
    nmfc: str = Field(description="NMFC Class (optional)")
    packUnit: str = Field(description="Type of packaging used (choice of BOX, BAIL, PALLET (more tbd))")
    packageCount: int = Field(description="Package Count. Ex: 1")
    flatPack: str = Field(description="Ships flat packed (choice of YES, NO). Ex: 'NO'")
    paletized: str = Field(description="Ships paletized (choice of YES, NO). Ex: 'NO'")
    length: float = Field(description="Overall shipment length (number). Ex: 3")
    width: float = Field(description="Overall shipment width (number). Ex: 3")
    height: float = Field(description="Overall shipment height (number). Ex: 8")
    girth: float = Field(description="Overall shipment girth (number). Ex: 20")
    weight: float = Field(description="Overall shipment weight (number). Ex: 2")
    cubeFt: float = Field(description="Shipment displacement in cubic feet (number)")
    cubeM: float = Field(description="Shipment displacement in cubic meters (number)")
    HsCode: str = Field(description="Harmonized commodity description. Ex: '6912.00.2500'")
    CisCode: str = Field(description="Canadian Customs Schedule code")

class Marketing(BaseModel):
    longDescription: str = Field(description="Long description of item. Ex: 'This amazing vase will change your life...'")
    keywords: list[str]= Field(description="Comma separated values for keywords. Ex: ['vase', 'copper', 'classic']")
    designer: str = Field(description="Designer name if available. Ex: 'Some Guy'")
    licensedName: str = Field(description="Licensed name if available")
    url: str = Field(description="Link to product on manufacturer's website. Ex: 'company.com/B2061ZZ'")
    seoTitle: str = Field(description="SEO content for websites. Ex: 'The must have vase for every home'")
    seoDescription: str = Field(description="SEO page title")
    seoKeywords: list[str]= Field(description="Meta description value (comma separated values)")

class Usage(BaseModel):
    indoor: str = Field(description="Is item suitable for indoor use? (choice of YES, NO). Ex: 'YES'")
    outdoor: str = Field(description="Is item suitable for outdoor use? (choice of YES, NO). Ex: 'NO'")
    uvResist: str = Field(description="Is item UV resistant? (choice of YES, NO). Ex: 'NO'")
    weatherResist: str = Field(description="Is item weather resistant? (choice of YES, NO)")
    waterResist: str = Field(description="Is item water resistant? (choice of YES, NO)")
    foodsafe: str = Field(description="Is item food safe? (choice of YES, NO)")
    commercial: str = Field(description="Is item commercial rated? (choice of YES, NO). Ex: 'YES'")
    adaCompliant: str = Field(description="Is item ADA Compliant? (choice of YES, NO)")
    installRequired: str = Field(description="Is installation required? (choice of YES, NO). Ex: 'NO'")
    assemblyRequired: str = Field(description="Is assembly required? (choice of YES, NO)")
    toolsIncluded: str = Field(description="Are tools included for assembly? (choice of YES, NO)")
    intendedEnvironment: str = Field(description="Recommended environment (choice of 'DRY', 'DAMP', 'WET', 'ANY'). Ex: 'Any'")
    ingressProtection: str = Field(description="IP protection rating. Ex: 'IP45'")
    ageGroup: str = Field(description="Suitable for age groups ('ADULT', 'CHILDREN', 'BABY', 'ANY'). Ex: 'ANY'")
    roomType: list[str] = Field(description="Room type (choice of Living Room, Dining Room, Bedroom, Bath, Hallway, Utility, Multi-Use, Outdoor)")
    careInstructions: str = Field(description="Care instructions")
    instructions: str = Field(description="Text description of the recommended care instructions")
    instructionUrl: str = Field(description="Link to public URL with care instructions")

class Environmental(BaseModel):
    statement: str = Field(description="Environmental information about the item (text)")
    recycled: str = Field(description="Is made from recycled materials? (choice of YES, NO). Ex: 'NO'")
    certification: str = Field(description="Certifications that the product has (text)")
    sustainability: str = Field(description="Sustainability statement (text)")
    fairtrade: str = Field(description="Is fairtrade certified? (choice of YES, NO). Ex: 'YES'")

class Compliance(BaseModel):
    warranty: str = Field(description="Warranty period (string). Ex: '2 years'")
    policy: str = Field(description="Warranty policy (text). Ex: 'blah blah'")
    policyLink: str = Field(description="Link to warranty policy (URL)")
    prop65: str = Field(description="Requires Prop65 Label (choice of YES, NO). Ex: 'YES'")

class Product(BaseModel):
    general_information: GeneralInformations
    spec: Spec
    product_class: ProductClass
    make: Make
    shipping: Shipping
    marketing: Marketing
    usage: Usage
    environmental: Environmental
    compliance: Compliance



from upsonic import ObjectResponse


class GeneralInformations_upsonic(ObjectResponse, GeneralInformations):
    pass

class ProductClass_upsonic(ObjectResponse, ProductClass):
    pass

class Spec_upsonic(ObjectResponse, Spec):
    pass

class Make_upsonic(ObjectResponse, Make):
    pass

class Shipping_upsonic(ObjectResponse, Shipping):
    pass

class Marketing_upsonic(ObjectResponse, Marketing):
    pass

class Usage_upsonic(ObjectResponse, Usage):
    pass

class Environmental_upsonic(ObjectResponse, Environmental):
    pass

class Compliance_upsonic(ObjectResponse, Compliance):
    pass

class Product_upsonic(ObjectResponse):
    general_information: GeneralInformations_upsonic
    spec: Spec_upsonic
    product_class: ProductClass_upsonic
    make: Make_upsonic
    shipping: Shipping_upsonic
    marketing: Marketing_upsonic
    usage: Usage_upsonic
    environmental: Environmental_upsonic
    compliance: Compliance_upsonic

