import json
import requests
import pandas


def request_products():
    url = "https://www.carecreations.basf.com/sitefinity/Public/Services/Products/ProductService.svc/GetCompactedProducts/"
    request = requests.get(url)
    products = json.loads(request.content)
    products_list = []
    for product in products:
        products_list.append({product["INCI_Name"]: product["sRelatedApplications"]})
    return products_list


# API_KEY = "x9kp2wln9uw22qzxu76e71jdbdil4d"
# API_ENDPOINT = "https://api.barcodelookup.com/v3/products"
# parameters = {
#     "barcode": "047677371156",
#     "formatted": "y",
#     "key": API_KEY
# }
#
# response = requests.get(API_ENDPOINT, params=parameters)
# response.raise_for_status()
# data = response.json()
# ingredients = data.get('products', 'no_products')[0].get('ingredients', 'no_ingredients')

deodorant = ["Alcohol Denat.",
             "Butane",
             "Isobutane",
             "Propane",
             "Parfum",
             "Zinc Neodecanoate",
             "Isopropyl Myristate",
             "Amyl Cinnamal",
             "Citral",
             "Citronellol",
             "Liminele",
             "Linalool"]

face_cream = ["Aqua (Water)",
              "Caprylic/Capric Triglycderide",
              "Cetyl Alcohol",
              "Propanediol Steary Alcohol",
              "Glycerin",
              "Sodium Hyaluronate",
              "Arginine",
              "Aspartic Acid",
              "Alenine",
              "Serine",
              "Valine",
              "Isoleucine",
              "Proline",
              "Threonine",
              "Histidine",
              "Phenylalanine",
              "Glucose",
              "Maltose",
              "Fructose",
              "Trehalose",
              "Sodium PCA",
              "PCA",
              "Sodium Lactate",
              "Urea",
              "Allantoin",
              "Linoleic Acid",
              "Oleic acid",
              "Phytosteryl Canola Glycerides",
              "Palmitic Acid",
              "Stearic Acid",
              "Lecithin",
              "Triolein",
              "Tocopherol",
              "Carbomer",
              "Isoceteth-20",
              "Polysorbate 60",
              "Sodium Chloride",
              "Citric Acid",
              "Trisodium Ethylenediamine",
              "Disuccinate",
              "Pentylene Glycol",
              "Triethanolamine",
              "Sodium Hydroxide",
              "Phenoxyethanol",
              "Chlorophenerin"]


tide_detergent = ["Sodium Laureth Sulfate",
                  "Sodium Silicoaluminate (Zeolite)",
                  "Sodium C12-15 Alkyl Sulfate",
                  "Silica"]

luvs_diaper = ["Petrolatum",
               "Stearyl Alcohol",
               "Aloe Barbadensis Leaf Extract"]


always_pads = ["Cellulose",
               "Polyester",
               "Sodium Polyacrylate",
               "Polyethylene",
               "Polypropylene",
               "Hot melt adhesive",
               "Titanium dioxide",
               "Ethylene Vinyl Acetate Copolymer",
               "PEG-7 Glyceryl Cocoate",
               "PEG-10 Cocoate",
               "PEG Sorbitol Hexaoleate",
               "PEG Hydrogenated Castor Oil Trilaurate",
               "Pigment Red 122",
               "Pigment Blue 15",
               "Pigment Violet 19",
               "Pigment Green 7",
               "Pigment Black 2",
               "Polyoxyalkylene Substituted Chromophore (violet)",
               "Polyoxyalkylene Substituted Chromophore (red)",
               "Fragrance"]


pantene = ["Sodium Citrate",
           "Citric Acid",
           "Sodium Citrate",
           "Tetrasodium EDTA",
           "Trisodium Ethylenediamine Disuccinate",
           "Dimethicone",
           "Stearyl Alcohol",
           "Cetyl Alcohol",
           "Sodium Laureth Sulfate",
           "Sodium Lauryl Sulfate",
           "Stearyl Alcohol",
           "Panthenol"]


oral_b = ["Glycerin",
          "Hydrated Silica",
          "Sodium Hexametaphosphate",
          "Propylene Glycol",
          "PEG-6",
          "Aqua",
          "Zinc Lactate",
          "Aroma",
          "Sodium Lauryl Sulfate",
          "Sodium Gluconate",
          "Silica",
          "Chondrus Crispus Powder",
          "CI 77891",
          "Trisodium Phosphate",
          "Stannous Fluoride",
          "Sodium Saccharin",
          "Xanthan Gum",
          "Sodium Fluoride",
          "Limonene",
          "CI 74160"]


sunscreen = ["AVENE THERMAL SPRING WATER (AVENE AQUA)",
             "C12-15 ALKYL BENZOATE",
             "DICAPRYLYL CARBONATE",
             "METHYLENE BIS-BENZOTRIAZOLYL TETRAMETHYLBUTYLPHENOL [NANO]",
             "WATER (AQUA)",
             "GLYCERIN",
             "BIS-ETHYLHEXYLOXYPHENOL METHOXYPHENYL TRIAZINE",
             "DIETHYLHEXYL BUTAMIDO TRIAZONE",
             "SILICA",
             "DIISOPROPYL ADIPATE",
             "BUTYL METHOXYDIBENZOYLMETHANE",
             "CETEARYL ISONONANOATE",
             "LAURYL GLUCOSIDE",
             "POLYGLYCERYL-2 DIPOLYHYDROXYSTEARATE",
             "DECYL GLUCOSIDE",
             "C10-18 TRIGLYCERIDES",
             "TRIMETHYLPENTANEDIOL/ADIPIC ACID/GLYCERIN CROSSPOLYMER",
             "ACRYLATES/C10-30 ALKYL ACRYLATE CROSSPOLYMER",
             "BENZOIC ACID",
             "BUTYLENE GLYCOL",
             "CAPRYLIC/CAPRIC TRIGLYCERIDE",
             "CAPRYLYL GLYCOL",
             "CITRIC ACID, DISODIUM EDTA",
             "FRAGRANCE (PARFUM)",
             "GLYCERYL BEHENATE",
             "GLYCERYL DIBEHENATE",
             "OXOTHIAZOLIDINE",
             "POTASSIUM CETYL PHOSPHATE",
             "PROPYLENE GLYCOL",
             "SODIUM BENZOATE",
             "SODIUM HYDROXIDE",
             "TOCOPHEROL",
             "TOCOPHERYL GLUCOSIDE",
             "TRIBEHENIN",
             "XANTHAN GUM"]


for ing in range(len(sunscreen)):
    title_ing = sunscreen[ing].title()
    sunscreen[ing] = title_ing

# print(data)
# ingredients_list = deod_ingredients.split(",")
# for i in ingredients_list:
#     new_i = i.find(":") + 1
#     # Falta imprimir a lista de ingredientes limpa
#     print(i[new_i:].strip().replace(".", ""))
# print(ingredients_list)


list_basf_products = request_products()
df = pandas.DataFrame(list_basf_products)


matches = list(set(df).intersection(sunscreen))
print("Ingredients in this product that BASF produces:")
for ing in matches:
    print(ing)
percentage = int(len(matches) / len(sunscreen) * 100)
basf_share = int(percentage * 0.38)
print(f"The product you're scanning has ca. {percentage}% of products that BASF produces.")
print(f"This means that you may be buying a product that was {basf_share}% made in BASF.")
print("Congratulations on choosing a Sustainable and Innovative solution for your daily life!")

# print(matches)