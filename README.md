# CLOUD COMPUTING (Aprendizaje Federado) 


## Autores:

- Nombre del equipo: BookML.
- Repositorio de Github: https://github.com/sheldon7681/federated-models.git 
- Miembros:
    - Luis Angel: 
    - Jorge Rocha: 
    - Pamela Ruiz: 
    - Gadiel Wisar: 
    - Azahel Ramirez: 

## Instalación: 

### Pre-requisitos

- Python 3.11
- (uv)[https://docs.astral.sh/uv/getting-started/installation/]


#### Pasos:

1. Clonar el repositorio 

```
git clone https://github.com/sheldon7681/federated-models.git

```


2. Instalar las dependencias 
```
uv sync
```

## Instruciones:

1. Descargar los datos y separarlos en n folds y ponerlos en el folder ```data``` 

2. Correr el notebook con el nombre ```entrenamiento_local.ipynb ``` y guardar los modelos ```models```

3. Correr el notebook ```entrenamiento_global.ipynb```

## Ensayo sobre resultados

Tras haber realizado distintas técnicas de aprendizaje federado, se encontró que posiblemente los modelos locales hayan sufrido de overfitting con respecto a la división realizada, dado que, no pudieron generalizar las predicciones con respecto a los datos de prueba que nunca habían visto. 

También puede que haya existido algún tipo de sesgo entre las divisiones, es decir, que en el fold 1 se escribiera algún número de cierta forma específica, lo cual haya afectado a los valores de los pesos a considerar que el número n tenga cierta forma definida y al momento de promediar los pesos haya habido confusión con respecto a la verdadera forma de los números.

Finalmente se encontró que IDA (Inverse Distance Aggregation) resultó ser el mejor modelo global, esto debido a su forma de normalizar la suma de las distancias inversas, lo cual reduce el probable sesgo entre grupos, de igual manera sería interesante intentar otras técnicas de aprendizaje federado para efectivamente lograr un modelo global que pueda realmente generalizar el aprendizaje.



