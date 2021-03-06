function calcular_tiempo_descanso(){
  t_ejercicio = document.getElementById('t_actividad').value
  if(t_ejercicio >= 20 && t_ejercicio <= 60){
    t_descanso = 60 - parseInt(t_ejercicio)
    document.getElementById('t_descanso').value = t_descanso
  }
}

function set_tiempo_inicial(){
  m = document.getElementById('tiempo').value;
  s = 0;
}

window.onload = init;
function init(){

    calcular_tiempo_descanso();
    set_tiempo_inicial();

    document.querySelector(".start").addEventListener("click",cuentaAtras);
    document.querySelector(".stop").addEventListener("click",parar);
    document.querySelector(".reiniciar").addEventListener("click",reiniciar);

    document.getElementById("ms").innerHTML="00:00";
}

function cuentaAtras(){
    document.getElementById('tiempo').disabled = true;
    document.getElementById('t_actividad').disabled = true;
    escribir();
    id = setInterval(escribir,1000);
    document.querySelector(".start").removeEventListener("click",cuentaAtras);
}

function escribir(){
    var mAux, sAux;
    alarma = document.getElementById('alarma')

    if (s == 0){
      m--;
      s=60;
      // Sonar alarma empezar activida
      console.log("Empezar actividad")
      alarma.play();
    }
    s--;

    if(s == 60 - 7 || s == document.getElementById('t_descanso').value - 7){
      alarma.pause();
      alarma.currentTime = 0;
    }

    if(s == document.getElementById('t_descanso').value){
      // Sonar alarma para descanso
      console.log("Empezar descanso")
      alarma.play();
    }

    if (s<10){sAux="0"+s;}else{sAux=s;}
    if (m<10){mAux="0"+m;}else{mAux=m;}

    document.getElementById("ms").innerHTML = mAux + ":" + sAux;

    if(s == 0 && m == 0){
      parar();
      reiniciar();
      console.log('Terminó el tiempo')
      //Redirigir a la dirección para guardar el registro de ejercicio
      enviar_datos()
    }
}
function parar(){
    clearInterval(id);
    alarma.pause()
    document.querySelector(".start").addEventListener("click",cuentaAtras);
    document.getElementById('tiempo').disabled = false;
    document.getElementById('t_actividad').disabled = false;
}

function reiniciar(){
  document.getElementById('tiempo').disabled = false;
  document.getElementById('t_actividad').disabled = false;

  alarma.pause();
  alarma.currentTime = 0;

  enviar_datos()

    clearInterval(id);
    document.getElementById("ms").innerHTML="00:00";
    m=document.getElementById('tiempo').value;
    s=0;
    document.querySelector(".start").addEventListener("click",cuentaAtras);
}

function enviar_datos(){
  var tneto = document.getElementById('tiempo').value
  var tjob = (tneto - m - 1)*60 + 60 - s
  var texe = document.getElementById('t_actividad').value
  var trest = document.getElementById('t_descanso').value

  location.href = "http://localhost:5000/work/save?tneto="+tneto+"&tjob="+tjob+"&texe="+texe+"&trest="+trest
}
