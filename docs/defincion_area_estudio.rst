Definci�n del �rea de Estudio
=============================


Criterios para Definir un �rea de Estudio
------------------------------------------

Para definir un �rea de estudio se deben tomar en cuenta los siguientes criterios:

* Ojetivo del estudio.

* La escala de los datos vectoriales de entrada. 

* El tama�o m�ximo de celda de los datos raster de entrada.

* La distancia m�xima que que se quiere evaluar fuera del �rea de estudio.


Ejemplo: Area de Estudio para Proyecto Tur�stico en el Valle
------------------------------------------------------------

Objectivo:Se desea ubicar un globo de terreno para ubicar un proyecto tur�stico.

La escala de los datos var�na entre 1:250,000 y 1:50,000.

El tama�o m�ximo de celda es de 90 m.

La distancia m�xmia fuera del �rea de estudio es de 2 km.


#. Abra ArcMap y cargue los temas que estan el la carpeta **El_Valle**.

   .. figure:: images/definicion_area_estudio_002.png

      Listado de Temas a Cargar
#. Haga clic en el menu **Selection\\Select by Attributes**.

   a. Seleccione el tema Corregimiento en **Layer**.
   #. Haga doble clic en **"NAME"**.
   #. Haga clic en el bot�n **Get Unique Values**.
   #. Seleccione **'EL VALLE'**
   #. Haga clic en Apply.

   .. figure:: images/definicion_area_estudio_004.png

      Selecci�n de Corregimiento de El Valle
#. Haga clic derecho sobre el tema **corregimientos_el_valle** y seleccione **Selection\\Create Layer From Selected Features**

   .. figure:: images/definicion_area_estudio_006.png

      Creando una capa con solo El Valle
   
   Le debe aparece un tema con el nombre **corregimientos_el_valle_Selection**. De ser necesario haga zoom para centrearlo y debe ver algo como esto.

   .. figure:: images/definicion_area_estudio_008.png

      Corregimiento del Valle.

#. Encienda el tema **curvas_nivel_el_valle_wgs84** y seleccione la curva de nivel **200**.

   .. figure:: images/definicion_area_estudio_010.png

      Curva de Nicel 200.

#. Haga clic derecho sobre el tema **curvas_nivel_el_valle_wgs84** y seleccione **Data\\Export Data**

   .. figure:: images/definicion_area_estudio_012.png

      Export Data

#. Guarde en el campo **Output feature class** seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_linea_wgs84.shp**.

   .. figure:: images/definicion_area_estudio_014.png

      Nombre del tema del �rea de estudio.

      Haga clic en el bot�n **Yes**

   .. figure:: images/definicion_area_estudio_016.png

      Cargar los datos exportados a ArcMap

#. En ArcToolbox abra la herramienta **Feature to Polygon**.

   a. Seleccione **area_estudio_linea_wgs84** en **Input Features** .

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_poli_wgs84.shp** en **Output Feature Class**.

   #. Haga clic en el bot�n **Ok**.

   .. figure:: images/definicion_area_estudio_018.png

      Conversi�n del tema de l�neas a pol�gonos.

#. En ArcToolbox abra la herramienta **Buffer**.
   
   a. Seleccione  **area_estudio_poli_wgs84** en **Input Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_poli_bf2k_wgs84.shp** en **Output feature class** .

   #. Digite **2** en **Linea Unit** y seleccione **Kilometers**.
   
   #. Haga clic en el bot�n **Ok**.

   .. figure:: images/definicion_area_estudio_020.png

      Par�metros para crear el Buffer del �rea de Estudio

   .. figure:: images/definicion_area_estudio_022.png

      Buffer del �rea de Estudio

#. En ArcToolbox abra la herramienta **Clip**.

   a. Seleccione **dem_pma_utm** en **Input Raster**.

   #. Seleccione **area_estudio_poli_bf2k_wgs84** en **Output Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\raster\\dem_valle** en **Output Raster Dataset**.

   #. Haga clic en el bot�n **Ok**.

   .. figure:: images/definicion_area_estudio_024.png

      Par�metros para realizar el Clip del DEM.

#. En ArcToolbox abra la herramienta **Feature Envelope to Polygon**.

   a. Seleccione  **area_estudio_poli_bf2k_wgs84** en **Input Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_rect_wgs84.shp** en **Output Feature Class**.

   #. Haga clic en el bot�n **Ok**.

   .. figure:: images/definicion_area_estudio_026.png

   P�rametros para genera el pol�gono de la extension del �rea de estudio

   El resultado es un rectangulo parecido a este:

   .. figure:: images/definicion_area_estudio_028.png

   Extensi�n del �rea de estudio.

