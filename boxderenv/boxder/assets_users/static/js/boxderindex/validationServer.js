function dataFromServer(data){
    
    // Usuario agregado correctamente
    if(data == '1'){ 
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro con éxito',
            showConfirmButton: true
          }).then(()=>{
            location.href = "../boxder";
          });   

    // Error al validar datos
    }else if( data == '0'){ 
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'No se han podido procesar los datos',
          });

    // Error de integridad de datos
    }else if(data == '2'){  
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: '¡Datos repetidos!',
          });

    // Error de servidor      
    }else if(data == '3'){  
    Swal.fire({
        icon: 'error',
        title: 'Error interno',
        text: 'Ha ocurrido un error de servidor',
      });
      
    }else if(data == '4'){  
      Swal.fire({
      icon: 'error',
      title: 'Error interno',
      text: 'No se encuentra la cedula',
    });
}};