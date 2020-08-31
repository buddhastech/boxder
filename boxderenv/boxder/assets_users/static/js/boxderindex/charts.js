
let statusCtx = document.getElementById('status-chart');

let statusChart  = new Chart(statusCtx, {
    type:"pie",
    data:{
        labels: ['Activo', 'Suspendido', 'De baja'],
        datasets:[{
            label: 'Activos',
            data: [6, 10, 2],
            backgroundColor:[
                "rgba(57, 127, 50, 0.9)",
                "rgba(255, 213, 0, 0.9)",
                "rgba(172, 38, 36, 0.9)"
                ]
            }]
        }
    });

    let priceCtx = document.getElementById('price-chart').getContext('2d');

    let chartPrice  = new Chart(priceCtx, {
        type:"bar",
        data:{
            labels: ['Enero', 'Febrero', 'Marzo', "Abril", "Mayo", "Junio"],
            datasets:[{
                label: 'Activos',
                data: [850, 3055, 7500, 2500, 29500, 754],
                backgroundColor:[
                    "rgba(246, 160, 115, 0.9)",
                    "rgba(50, 216, 14, 0.9)",
                    "rgba(36, 172, 135, 0.9)",
                    "rgba(36, 112, 172, 0.9)",
                    "rgba(90, 36, 172, 0.9)",
                    "rgba(216, 197, 14, 0.9)"
                    ]
                }]
            }
        });

        