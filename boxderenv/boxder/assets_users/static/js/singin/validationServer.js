function dataFromServer(data){
    
    if(data == '1'){ // Usuario agregado correctamente
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro con éxito',
            showConfirmButton: true
          }).then(() => {
            window.location.href = "../inicio";
          });
          
    }else if( data == '0'){ // Error al validar datos
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'No se han podido procesar sus datos',
          });

    }else if(data == '2'){  // Error de integridad de datos
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'Algunos datos ya existen y no pueden usarse',
          });
    }

}