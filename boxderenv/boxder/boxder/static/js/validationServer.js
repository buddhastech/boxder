function dataFromServer(data){
    
    // Error al validar datos
    if( data == '0'){ 
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'Ha ocurrido un error de servidor',
          });

    
    }else if(data == '1'){  
        Swal.fire({
            icon: 'error',
            title: 'Error interno',
            text: 'Lo sentimos, los credenciales no coinciden a ningún usuario',
          });
    }

};