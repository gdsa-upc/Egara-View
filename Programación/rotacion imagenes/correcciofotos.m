%Llegir totes les imatges de test (en aquest cas)
lee_archivos = dir('C:\Users\Gerard\Documents\Universidad\TercerCurso\GDSA\Proyecto\TerrassaBuildings900\TerrassaBuildings900\test\images\*.jpg');

%Bucle per modificar les imatges
for k = 1:length(lee_archivos)
    archivo = lee_archivos(k).name;
    nombre='C:\Users\Gerard\Documents\Universidad\TercerCurso\GDSA\Proyecto\TerrassaBuildings900\TerrassaBuildings900\test\images\';   
    correccio_angle(strcat(nombre,archivo),archivo);
    end
    
    
   
