# gabil-genetic-algorithms
Proyecto de algoritmos genéticos utilizando GABIL - Inteligencia Artificial 2

### Cómo correr el proyecto

En la carpeta _src/_ ejectutar el siguiente comando:

```
$ python main.py -p <inputPositiveFile> -n <inputNegativeFile> -s <selectionTypeParents> -e <selectionTypeSurvivors> -m <mutationRate> -c <crossoverRate> -x <penalization> -g <generations> -i <populationSize>
```

Donde:

1. **Input Positive File**: El archivo de los datos de la clase positiva (+).
2. **Input Negative File**: El archivo de los datos de la clase negativa (-).
3. **Selection Type Parents**: El tipo de selección de padres.

  * 1 -> Rueda de ruleta.
  * 2 -> Selección por rango.
  * 3 -> Selcción por torneo. 

4. **Selection Type Survivors**: El tipo de selección de sobrevivientes.

  * 0 -> Sin elitismo.
  * 1 -> Con elitismo.

5. **Mutation Rate**: La tasa de mutación.
6. **Crossover Rate**: La tasa de crossover.
7. **Penalization**: Opción para penalizar o no.

  * 0 -> No hay penalización.
  * 1 -> Hay penalización.
 
8. **Generations**: Número de generaciones.
9. **Population Size**: Tamaño de la población.
  
Los únicos parámetros obligatorios son los de los archivos de datos. Los valores por defecto son los siguientes:

* **Crossover**: 0.8
* **Mutuación**: 0.01
* **Selección de padres**: rueda ruleta
* **Selección de sobrevivientes**: sin elitismo.
* **Penalización**: sin penalización.
* **Generaciones**: 1000
* **Población**: 20


#### Ejemplos de corridas:


```
$ python main.py -p positive.data -n negative.data
```
```
$ python main.py -p positive.data -n negative.data -c 0.8 -m 0.01 -e 1 -i 60 -s 2
```

### Organización del Repositorio

_data/_ : Donde se encuentran los conjuntos de datos disponibles para este proyecto.

_docs/_ : Documentos necesarios para el proyecto.

_graphs/_ : Gráficos que se realizaron para el informe.

_src/_ : Donde está el código fuente.

_tests/_: Directorio con los resultados de todas las corridas.
