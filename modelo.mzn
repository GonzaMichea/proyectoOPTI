%Cantidad de asignaturas: n. Y cantidad de salas: m.
int: n;
int: m;

%Conjuntos
set of int: ASIGNATURAS = 1..n; %i
set of int: BLOQUES = 1..7; %j
set of int: DIAS = 1..5; %k
set of int: SALAS = 1..m; %l

%Parámetros
array[ASIGNATURAS] of int: p; %Prioridad
array[ASIGNATURAS] of int: b; %Bloques requeridos
array[ASIGNATURAS, BLOQUES, DIAS] of int: r; %Bloques restringidos
array[ASIGNATURAS] of int: I; %Interesados
array[SALAS] of int: c; %Capacidad

%Variables
array[ASIGNATURAS, BLOQUES, DIAS, SALAS] of var int: x;
array[ASIGNATURAS] of var int: y;

%Restricciones
constraint forall(i in ASIGNATURAS)
                  (y[i] > (p[i]-6) div 10);
                  
constraint forall(j in BLOQUES, k in DIAS, l in SALAS)
                  (1 >= sum (i in ASIGNATURAS)(x[i,j,k,l]));
                  
constraint forall(i in ASIGNATURAS)
                  (sum (j in BLOQUES, k in DIAS, l in SALAS)(x[i,j,k,l]) = b[i]);
                  
constraint forall(i in ASIGNATURAS, j in 1..6, k in DIAS, l in SALAS)
                  (x[i,j,k,l] + x[i,j+1,k,l] = b[i]);

constraint forall(i in ASIGNATURAS, j in BLOQUES, k in DIAS, l in SALAS)
                  (x[i,j,k,l] <= r[i,j,k]);

constraint forall(i in ASIGNATURAS, j in BLOQUES, k in DIAS, l in SALAS)
                  (I[i] <= x[i,j,k,l]*c[l]);

%Función Objetivo
solve maximize sum(i in ASIGNATURAS)(y[i]*p[i]);