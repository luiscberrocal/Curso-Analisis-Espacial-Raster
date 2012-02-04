Definción del Área de Estudio
=============================


Criterios para Definir un Área de Estudio
------------------------------------------

Para definir un área de estudio se deben tomar en cuenta los siguientes criterios:

* Ojetivo del estudio.

* La escala de los datos vectoriales de entrada. 

* El tamaño máximo de celda de los datos raster de entrada.

* La distancia máxima que que se quiere evaluar fuera del área de estudio.


Ejemplo: Area de Estudio para Proyecto Turístico en el Valle
------------------------------------------------------------

Objectivo:Se desea ubicar un globo de terreno para ubicar un proyecto turístico.

La escala de los datos varína entre 1:250,000 y 1:50,000.

El tamaño máximo de celda es de 90 m.

La distancia máxmia fuera del área de estudio es de 2 km.


#. Abra ArcMap y cargue los temas que estan el la carpeta **El_Valle**.

   .. figure:: images/definicion_area_estudio_002.png

      Listado de Temas a Cargar
#. Haga clic en el menu **Selection\\Select by Attributes**.

   a. Seleccione el tema Corregimiento en **Layer**.
   #. Haga doble clic en **"NAME"**.
   #. Haga clic en el botón **Get Unique Values**.
   #. Seleccione **'EL VALLE'**
   #. Haga clic en Apply.

   .. figure:: images/definicion_area_estudio_004.png

      Selección de Corregimiento de El Valle
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

      Nombre del tema del área de estudio.

      Haga clic en el botón **Yes**

   .. figure:: images/definicion_area_estudio_016.png

      Cargar los datos exportados a ArcMap

#. En ArcToolbox abra la herramienta **Feature to Polygon**.

   a. Seleccione **area_estudio_linea_wgs84** en **Input Features** .

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_poli_wgs84.shp** en **Output Feature Class**.

   #. Haga clic en el botón **Ok**.

   .. figure:: images/definicion_area_estudio_018.png

      Conversión del tema de líneas a polígonos.

#. En ArcToolbox abra la herramienta **Buffer**.
   
   a. Seleccione  **area_estudio_poli_wgs84** en **Input Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_poli_bf2k_wgs84.shp** en **Output feature class** .

   #. Digite **2** en **Linea Unit** y seleccione **Kilometers**.
   
   #. Haga clic en el botón **Ok**.

   .. figure:: images/definicion_area_estudio_020.png

      Parámetros para crear el Buffer del área de Estudio

   .. figure:: images/definicion_area_estudio_022.png

      Buffer del área de Estudio

#. En ArcToolbox abra la herramienta **Clip**.

   a. Seleccione **dem_pma_utm** en **Input Raster**.

   #. Seleccione **area_estudio_poli_bf2k_wgs84** en **Output Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\raster\\dem_valle** en **Output Raster Dataset**.

   #. Haga clic en el botón **Ok**.

   .. figure:: images/definicion_area_estudio_024.png

      Parámetros para realizar el Clip del DEM.

#. En ArcToolbox abra la herramienta **Feature Envelope to Polygon**.

   a. Seleccione  **area_estudio_poli_bf2k_wgs84** en **Input Features**.

   #. Seleccione **<Su Directorio>\\El_Valle\\vector\\area_estudio_rect_wgs84.shp** en **Output Feature Class**.

   #. Haga clic en el botón **Ok**.

   .. figure:: images/definicion_area_estudio_026.png

   Párametros para genera el polígono de la extension del área de estudio

   El resultado es un rectangulo parecido a este:

   .. figure:: images/definicion_area_estudio_028.png

   Extensión del área de estudio.

