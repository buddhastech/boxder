function dataFromServer(data){
    
    // Usuario agregado correctamente
    if(data == '1'){ 
        Swal.fire({
            position: 'center',
            icon: 'success',
            title: 'Registro con éxito',
            showConfirmButton: true
          }).then(() => {
            window.location.href = "../inicio";
          });

    // Error al validar datos
    }else if( data == '0'){ 
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'No se han podido procesar sus datos',
          });

    // Error de integridad de datos
    }else if(data == '2'){  
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'Algunos datos ya existen y no pueden usarse',
          });
    }

};