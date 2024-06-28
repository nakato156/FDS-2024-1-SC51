# Trabajo Final Fundamentos de Data Science

## Introduccion

Una conocida consultora extranjera, por requerimiento de su cliente, una empresa importante de marketing digital, desea conocer las tendencias de los videos de YouTube en el país de Alemania. Esta consultora necesita de tu ayuda para crear un modelo que permita que su cliente pueda obtener respuestas a varios requerimientos de información.
La consultora ha contratado tus servicios debido a tus habilidades en la Ciencia de Datos y tu especialidad en el modelado de regresión lineal. Este proyecto de analítica se llevará a cabo con el objetivo de identificar y analizar las tendencias de los videos de YouTube en Alemania, proporcionando información valiosa para la toma de decisiones estratégicas en marketing digital.

## Objetivo del proyecto

El objetivo principal del proyecto es desarrollar un modelo de datos que permita identificar las tendencias y patrones de consumo de videos en YouTube en Alemania. Se busca determinar cuáles son los temas más populares, el tipo de contenido que atrae a más espectadores, y cómo varían estas tendencias con el tiempo. Este análisis ayudará a la empresa cliente a optimizar sus campañas publicitarias y estrategias de contenido, adaptándolas a las preferencias y comportamientos del público alemán

A partir de la aplicación del modelo de regresión lineal y otras técnicas de análisis de datos, se espera extraer un conocimiento profundo y accionable que permita a la empresa cliente:

 + Comprender las Preferencias del Público Alemán: Identificar los intereses y preferencias de los usuarios en YouTube en Alemania.

+ Optimizar Estrategias de Contenido: Desarrollar estrategias de contenido alineadas con las tendencias identificadas, aumentando el engagement y el alcance de las campañas.


+ Predecir Tendencias Futuras: Utilizar el análisis de datos históricos para predecir posibles futuras tendencias y preparar campañas proactivas.

+ Segmentación de Audiencia: Mejorar la segmentación de la audiencia, permitiendo una personalización más efectiva de los mensajes y promociones.

## Integrantes

| Integrantes  | Codigo  | Puesto  |
| ------------- | ------------- |------------- |
| Bruno Alessandro Medina Agnini  | U202216661  | Business Project Sponsor - Data Engineer|
| Christian Aaron Velasquez Borasino  | U202218075 |Data Scientist |
|Joaquin Mauricio Eguia Castilla |   U202213539| Data Analytics|

## Breve descripcion de los datos

|Columna|Tipo de dato|Descripción|
| ------------- | ------------- |------------- |
|video_id|Object|Identificador único de los videos|
|trending_date|Object|Fecha en el cual el video fue tendencia|
|title|Object|Título del vídeo|
|channel_title|Object|Nombre del canal que subió el video|
|category_id|int64|Identificador de las categorías|
|publish_time|Object|Fecha de publicación del video en Youtube|
|tags|Object|Etiquetas del video|
|views|int64|Cantidad de vistas que tiene el video|
|likes|int64|Cantidad de likes que tiene el video|
|dislikes|int64|Cantidad de dislikes que tiene el video|
|comment_count|int64|Cantidad de comentarios que tiene el video|
|thumbnail_link|object|Enlace del video|
|comments_dissabled|bool|“Flag” que determina si los comentarios fueron desactivados o se mantienen activados.|
|ratings_disabled|bool|“Flag” que determina si la opción de calificar un video está desactivada o no.|
|video_error_or_removed|bool|“Flag” que determina si el video tiene un error o si fue eliminado, o si sigue disponible.|
|description|object|Breve descripción del video.|
|state|object|Nombre del Estado perteneciente al país.|
|lat|float64|Latitud geográfica de ubicación del Estado.|
|lon|float64|Longitud geográfica de ubicación del Estado|
|geometry|object|Registra las coordenadas de las geometrías donde se ubica el Estado dentro del planeta. Es de utilidad si se decide utilizar la librería GeoPandas para la elaboración de mapas.|

## Conclusiones

+ Por Categoría de Videos 
    + ¿Qué categorías de videos son las de mayor tendencia? 

            Las categorías más vistas son la 24 y la 22, siendo la mayor de estas la 24 la cual es Entertainment. Mientras que la 22 es  People & Blogs.
            El hecho que Entertainment sea la categoría por más tendencias significa que la gente tiende a buscar con preferencia los canales cuyo contenido sea de cualquier tipo de entretenimiento, ya sea comedia, deportes, etc.

    + ¿Qué categorías de videos son los que más gustan? ¿Y las que menos gustan? 
            
            La categoría con más me gustas es la categoría 10, la que es Music, la gran cantidad de likes que tienen nos puede ayudar a definir que, un canal que hable de música, mientras suba contenido de calidad, será bien valorado y recibido por los usuarios de la plataforma.
            Y la categoría con más “No me gusta” es la 32, la cual es Action/Adventure, algo sorprendente pero significa que los usuarios en Alemania no son muy fanáticos de esta categoría por lo cual, si quieres dedicarte a Youtube, no subas esta categoría de videos.

    + ¿Qué categorías de videos tienen la mejor proporción (ratio) de “Me gusta” / “No me gusta”? 

        Las categorías con mejor ratio de Me gustas y no me gusta son las categorías 1, 2, 10, 15, 17.
        
            La 1 es Film & Animation, es la 3ra con mejor ratio, esta puede tener una audiencia apasionada y fiel que aprecia la diversidad de contenido, desde animaciones independientes hasta reseñas y teorías sobre películas. Esta audiencia puede ser más propensa a interactuar positivamente con el contenido y a seguir a sus creadores favoritos.
            
            La 2 es Autos & Vehicles, es la 4ta con mejor ratio, esto indica que los espectadores de estos videos generalmente están muy satisfechos con el contenido que ven. Esto sugiere que el contenido de esta categoría es bien recibido y valorado positivamente por la audiencia. 

            La 10 es Music, es la que tiene mejor ratio entre todas las categorías, la música suele ser una categoría universalmente popular entre tu audiencia o grupo de datos. Esto sugiere que las publicaciones relacionadas con música tienden a resonar más positivamente que otras categorías. Lo cual podría ayudar a nuevos “Youtubers” a elegir el tipo de video que quieren empezar a subir.

            La 15 es Pets & Animals, es la 5ta con mejor ratio, de esta categoría se pueden sacar varias cosas. Las publicaciones que incluyen mascotas, animales lindos o historias relacionadas con ellos tienen más probabilidades de generar una respuesta positiva. Este tipo de contenido tiende a resonar emocionalmente con la audiencia, lo que puede aumentar la interacción y compartir entre los seguidores. Además de que las historias divertidas, tiernas o inspiradoras sobre mascotas y animales tienen un potencial considerable para volverse virales, lo cual podría ser una ventaja estratégica al planificar campañas de contenido o estrategias de redes sociales

            La 17 es Sports, la 2da con mejor ratio, esto muestra que la audiencia muestra un fuerte interés en contenido relacionado con deportes. Esto sugiere que las publicaciones sobre eventos deportivos, noticias o análisis pueden generar una respuesta positiva y compromiso entre los seguidores. Esto podría ayudarnos a definir fechas para subir nuevos videos, ya que podríamos alinearnos con los eventos deportivos y subir ahí nuevo material.

    + ¿Qué categorías de videos tienen la mejor proporción (ratio) de “Vistas” / “Comentarios”?

            El que tiene mejor ratio es Movies, esto sugiere que la audiencia tiene un fuerte interés en contenido relacionado con películas. Esto incluye noticias de cine, críticas, análisis de películas, trailers y cualquier otra forma de contenido cinematográfico. Puedes explorar diferentes géneros de películas, tendencias cinematográficas actuales, y colaboraciones con actores o directores para diversificar y enriquecer tu contenido en esta categoría.
            Y la categoría que peor ratio tiene es Gaming, esto puede ser ya que la comunidad de videojuegos suele ser algo tóxica o muy pegada a la antigua, los antiguos jugadores no aceptan a los nuevos y eso puede conllevar a menos comentarios o incluso más comentarios (malos comentarios).

+ Por el tiempo transcurrido 
    + ¿Cómo ha cambiado el volumen de los videos en tendencia a lo largo del tiempo?

            Se observan varios picos altos en diferentes momentos (como a finales de diciembre de 2017, en febrero de 2018 y en mayo de 2018). Estos picos indican periodos donde ciertos videos se volvieron muy populares, posiblemente debido a eventos específicos o lanzamientos de videos virales. Algunos de estos eventos famosos que se dieron entre esa época de año son “Desafío de la caja misteriosa”, “The floor is Lava”, “Invisible Box”, “Baile de Fornite”.
            Aunque hay fluctuaciones, parece haber una ligera tendencia al alza en las vistas a lo largo del tiempo. Esto podría indicar un crecimiento general en el interés por los videos o un incremento en el número de usuarios de YouTube.

+ Por Canales de YouTube
    + ¿Qué canales de YouTube son tendencia más frecuentemente? ¿Y cuáles con menos frecuencia? 

            El canal más frecuente es el de Galileo, esto puede significar que es muy popular en Alemania. Esto se puede tomar como ventaja al querer hacer alguna colaboración o publicidad con este canal, ya que será exitoso en el ámbito de exposición ya que el canal tiene bastante alcance.
            En los menos frecuentes están Soz Dizi y The Daily Show with Trevor Noah, canales menos buscados, posiblemente por pertenecer a categorías no populares. Las empresas que quieran hacer colaboraciones con estos canales deberían pensarlas bien, ya que podrían no tener el grado de exposición que quisieran.

+ Por la geografía del país 
    + ¿En qué Estados se presenta el mayor número de “Vistas”, “Me gusta” y “No me gusta”?

            El mayor número de vistas se presenta en los estados de Bremen, Renania Norte-Westfalia y Hesse, siendo Bremen el mayor.
            El mayor número de Me gustas se presenta en los estados de Bremen, Renania Norte-Westfalia, Hesse y Brandenburgo, siendo Bremen el mayor.
            El mayor número de No Me gusta se presenta en los estados de Renania Norte-Westfalia y Brandenburgo. 

+ Adicionalmente, al cliente le gustaría conocer si: 
    + ¿Es factible predecir el número de “Vistas” o “Me gusta” o “No me gusta”? 
Vistas

        El modelo tiene una capacidad limitada para predecir el número de visitas, un R² Score de 0.56 indica aproximadamente el 56% de la variabilidad en el número de vistas puede ser explicada por el modelo, lo cual sugiere que aún hay un margen significativo para mejorar la precisión del modelo.

    + Likes

        El modelo es relativamente mejor para predecir el número de "Me gusta", con un R² Score de 0.67. Esto significa que el 67% de la variabilidad en los "Me gusta" es explicada por el modelo, lo cual es un buen indicativo de su capacidad predictiva, aunque aún puede mejorar.

    + Dislike

        El modelo tiene una capacidad limitada para predecir el número de "No me gusta", con un R² Score de 0.43. Esto indica que solo el 43% de la variabilidad en los "No me gusta" puede ser explicada por el modelo, sugiriendo que se necesita un refinamiento significativo para mejorar su precisión.

    + ¿Los videos en tendencia son los que mayor cantidad de comentarios positivos reciben?

        Observando la gráfica se podría decir que sí, se evidencia que cuando un video llega a ser tendencia 2 veces, llega a alcanzar en promedio 90 comentarios positivos.
        Aunque también se evidencia que hubo un caso donde con ser solamente 1 vez tendencia, llegó a tener casi 100 comentarios positivos.
