
window.addEventListener('DOMContentLoaded', async(event) => {
    console.log('DOM fully loaded and parsed');
    const res = await fetch('/static/types.json')
    const data = await res.json()
    const auto = Object.keys(data)
    auto.sort((a, b) => a.length - b.length);
    const autoCompleteJS = new autoComplete({
        selector: "#autoComplete",
        placeHolder: "Search for columns...",
        data: {
            src: auto,
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
    document.getElementById('autoComplete').value = '';
    const arr = [...new Set(values)]
    let txt = ''
    arr.forEach(column=>{
        txt += `${column}, `
    })
    document.getElementById('columns').innerHTML = txt;
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
