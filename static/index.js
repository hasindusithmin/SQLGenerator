
window.addEventListener('DOMContentLoaded', async(event) => {
    console.log('DOM fully loaded and parsed');
    const res = await fetch('/static/types.json')
    const data = await res.json()
    const autoCompleteJS = new autoComplete({
        selector: "#autoComplete",
        placeHolder: "Search for columns...",
        data: {
            src: Object.keys(data),
            cache: true,
        },
        resultItem: {
            highlight: true
        },
        events: {
            input: {
                selection: (event) => {
                    const selection = event.detail.selection.value;
                    autoCompleteJS.input.value = selection;
                }
            }
        }
    });

});

let values = []
document.getElementById('add').onclick = ()=>{
    const column = document.getElementById('autoComplete').value;
    if (column != '') {
        values.push(column);
    }
    document.getElementById('autoComplete').value = ''
    console.log(values)
}

document.getElementById('generate').onclick = ()=>{
    let columns = ''
    const arr = [...new Set(values)]
    arr.forEach(column=>{
        columns += column + ','
    })
    const table = document.getElementById('table').value;
    const qty = document.getElementById('qty').value;
    
    if (table != '' && qty != '' && columns != '') {
        const url = `/gensql/${table}?qty=${qty}&columns=${columns}`
        location.href = url;
    }

}
