window.onload = calcular_tiempo_descanso

function calcular_tiempo_descanso(){
  t_ejercicio = document.getElementById('t_actividad').value
  if(t_ejercicio >= 20 && t_ejercicio <= 60){
    t_descanso = 60 - parseInt(t_ejercicio)
    document.getElementById('t_descanso').innerHTML = "Tiempo de descanso: " + t_descanso + " segundos"
  }
}
