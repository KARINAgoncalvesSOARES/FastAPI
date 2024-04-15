# run: uvicorn FastAPI:app --reload
# Interactive API docs: localhost:8000/docs
# Alternative API docs: localhost:8000/redoc

from fastapi import FastAPI
from fastapi import Query, HTTPException
import uvicorn
import os
import pickle

import warnings
warnings.simplefilter("ignore")


app = FastAPI()

@app.get("/")
def home():
    return {
        "Projeto": "Previsão de aplicativo de supermercado preferível na Hungria 🛒 🇭🇺",
        "Objetivo": "Aplicativo Educacional",
        "Versão": "0.1.0"
    }

@app.get("/predict")
def predict(Gender: int = Query(..., description="Gênero: 1 para masculino, 2 para feminino"),
            Education: int = Query(..., description="Nível de escolaridade: 1 para graduação, 2 para associate, 3 para bacharelado, 4 para mestrado, 5 para doutorado"),
            Age: int = Query(..., description="Idade do usuário"),
            Exp_online: int = Query(..., description="Anos de experiência com compras online"),
            Exp_app: int = Query(..., description="Anos de experiência no uso de aplicativos de supermercado")):
    """
    Prevê o aplicativo de supermercado com base nas entradas do usuário.

     Parâmetro age: Idade do usuário. 
     
     Parâmetro  gender: Gênero do usuário (1 para homem, 2 para mulher). 
     
     Parâmetro education: Nível de escolaridade do usuário (1 para graduação, 2 para associado, 3 para bacharelado, 4 para mestrado, 5 para doutorado). 
     
     Parâmetro  exp_online: Anos de experiência com compras online. 
     
     Parâmetro exp_app: Anos de experiência no uso de aplicativos de supermercado. 
    """
   # Verifique se os valores de gênero e educação estão dentro do permitido
    if Gender not in [1, 2] or Education not in [1, 2, 3, 4, 5]:
        raise HTTPException(status_code=400, detail="Entrada inválida. O sexo deve ser 1 ou 2 e a educação deve estar entre 1 e 5.")

    # Verifica se todas as entradas são números inteiros
    if not all(isinstance(val, int) for val in [Gender, Education, Age, Exp_online, Exp_app]):
        raise HTTPException(status_code=400, detail="Somente entradas inteiras são permitidas.")

    #  Carrega o caminho absoluto do modelo
    class_app_names = ["FoodPanda", "Wolt", "Spar", "Tesco Online", "myLidl"]
    model_path = os.path.join(os.getcwd(), '/home/karinag/karina_python/github/FastAPI/2_fastapi/clf_silple.pkl')
    loaded_model = pickle.load(open(model_path, 'rb'))
    
    prediction = loaded_model.predict([[Gender, Education, Age, Exp_online, Exp_app]])
    predicted_app = class_app_names[int(prediction[0])]
    
    return {'O aplicativo de mercearia previsto é': predicted_app}

if __name__ == "__main__":
    uvicorn.run(app)