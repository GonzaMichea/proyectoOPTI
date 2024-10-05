%Lectura de datos

%ESCRIBAN AQUÍ CÓMO SE VAN A LLAMAR LAS LISTAS

%Variables
array[1..n, 1..35, 1..m] of var bool: x;

array[1..n] of var bool: y;

%%%%%%%%%%%%%%
%Restricciones
%%%%%%%%%%%%%%

%Asignaturas indispensables
constraint forall(i in 1..n)(
    y[i] > (p[i] - 6) / 10
);

%Asignación de asignaturas a una única sala
constraint 



