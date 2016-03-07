# gabil-genetic-algorithms
Proyecto de algoritmos genéticos utilizando GABIL - Inteligencia Artificial 2

### Cómo correr el proyecto

En la carpeta _src/_ ejectutar el siguiente comando:

```
$ python main.py -f <inputFile> -p <selectionTypeParents> -s <selectionTypeSurvivors> -m <mutationRate> -c <crossoverRate> -x <penalization> -g <generations> -n <populationSize>
```

Donde:

1. **Input file**: El archivo a clasificar.
2. **Selection Type Parents**: El tipo de selección de padres.

  * 1 -> Rueda de ruleta.
  * 2 -> Selección por rango.
  * 3 -> Selcción por torneo. 

3. **Selection Type Survivors**: El tipo de selección de sobrevivientes.

  * 0 -> Sin elitismo.
  * 1 -> Con elitismo.

4. **Mutation Rate**: La tasa de mutación.
5. **Crossover Rate**: La tasa de crossover.
6. **Penalization**: Opción para penalizar o no.

  * 0 -> No hay penalización.
  * 1 -> Hay penalización.
 
7. **Generations**: Número de generaciones.
8. **Population Size**: Tamaño de la población.
  

#### Ejemplos de corridas:


```
$ python main.py -f crx.data
```
```
$ python main.py -f crx.data -p 1 -s 1 -m 0.2 -c 0.8 -x 0
```

### Organización del Repositorio

_data/_ : Donde se encuentran los conjuntos de datos disponibles para este proyecto.

_docs/_ : Documentos necesarios para el proyecto.

_graphs/_ : Gráficos que se realizaron para el informe.

_src/_ : Donde está el código fuente.
