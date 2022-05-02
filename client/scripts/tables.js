var tableSelect = $('#table-select')
var selectedTable = tableSelect.find(":selected").text()
var tableFirstLine = $('#table-first-line')
var tableBody = $('#table-body')
var keys
createTable(selectedTable)

tableSelect.on("change", () => {
    selectedTable = tableSelect.find(":selected").text()
    console.log(selectedTable)
    createTable(selectedTable)
})


function createTable(tableName) {
    fetch("http://127.0.0.1:5000/" + tableName)
        .then(resp => resp.json())
        .then(data => {
            tableFirstLine.empty()
            tableBody.empty()
            console.log(data)

            keys = Object.keys(data[0])
            for (key of keys) {
                tableFirstLine.append(`<th scope="col">${key}</th>`)
            }
            tableFirstLine.append(`<th scope="col">Törlés</th>`)
            tableFirstLine.append(`<th scope="col">Szerkesztés</th>`)

            createInsertForm(keys)
            for (d of data) {
                let buttonId = `${d["ID"]}`
                //ticket esetén összetet kulcs van
                
                if (selectedTable == "ticket"){
                    buttonId = `${d["USER_ID"]}-${d["TRIP_ID"]}`
                }
                
                let tr = "";
                for (key of keys) {
                    tr += `<td>${d[key]}</td>`
                }
                tr += `<td><button type="button" class="btn btn-danger" id="delete-${buttonId}">Törlés</button></td>`
                tr += `<td><button type="button" class="btn btn-success" id="edit-${buttonId}">Szerkesztés</button></td>`
                tableBody.append(`<tr>${tr}</tr>`)
                $(`#delete-${buttonId}`).on("click", deleteElement)
                $(`#edit-${buttonId}`).on("click", editElement)
            }
        })
}

function createInsertForm(keys) {
    tr = `<td><button type="button" class="btn btn-primary" id="insert" style="background-color:red">Új</button></td>`
    for (key of keys) {
        if (key !== "ID") {
            tr += `<td><input  class="form-control" type="text" id=${key} name=${key}></td>`
        }
    }
    tableBody.append(tr)
    $('#insert').on("click", insertElement)
}


function insertElement() {
    params = {}
    for (key of keys) {
            if(key !== "ID"){
                params[key.toLowerCase()] = $("#" + key).val()
            }
    }

    fetch("http://127.0.0.1:5000/" + selectedTable , {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(params)
    })
}


function deleteElement() {

    let id, user_id, trip_id
    //ticket esetén összetet kulcs van
    if(selectedTable == "ticket"){
        user_id = $(this).attr('id').split("-")[1]
        trip_id = $(this).attr('id').split("-")[2]
        req = {user_id: user_id, trip_id:trip_id}
    }else{
        id = $(this).attr('id').split("-")[1]
        req = {id:id}
    }

    fetch("http://127.0.0.1:5000/" + selectedTable, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(req)
    })
}

function editElement() {
    let id = $(this).attr('id').split("-")[1]
    console.log($(this).attr('id'))
    fetch("http://127.0.0.1:5000/" + selectedTable)
        .then(resp => resp.json())
        .then(data => {
            tableFirstLine.empty()
            tableBody.empty()
            console.log(data)

            keys = Object.keys(data[0])
            for (key of keys) {
                tableFirstLine.append(`<th scope="col">${key}</th>`)
            }
            tableFirstLine.append(`<th scope="col">Törlés</th>`)
            tableFirstLine.append(`<th scope="col">Szerkesztés</th>`)

            createInsertForm(keys)
            for (d of data) {
                let buttonId = `${d["ID"]}`
                if(buttonId==id){ //szerkesztesz?
                    let tr = `<td>${d["ID"]}</td>`;
                    for (key of keys) {
                        if (key !== "ID") {
                        tr +=`<td><input  class="form-control" type="text" id=${key}_${d["ID"]} name=${key}_${d["ID"]} value='${d[key]}'></td>`
                        }
                    }
                    tr += `<td><button type="button" class="btn btn-danger" id="delete-${buttonId}">Törlés</button></td>`
                    tr += `<td><button type="button" class="btn btn-success" id="edit-${buttonId}">Mentés</button></td>`
                    tableBody.append(`<tr>${tr}</tr>`)
                    $(`#delete-${buttonId}`).on("click", deleteElement)
                    $(`#edit-${buttonId}`).on("click", saveEditedElement)
                }else{
                    let tr = "";
                    for (key of keys) {
                        tr += `<td>${d[key]}</td>`
                    }
                    tr += `<td><button type="button" class="btn btn-danger" id="delete-${buttonId}">Törlés</button></td>`
                    tr += `<td><button type="button" class="btn btn-success" id="edit-${buttonId}">Szerkesztés</button></td>`
                    tableBody.append(`<tr>${tr}</tr>`)
                    $(`#delete-${buttonId}`).on("click", deleteElement)
                    $(`#edit-${buttonId}`).on("click", editElement)
                }
            }
        })
}
function saveEditedElement(){
    let id = $(this).attr('id').split("-")[1]
    params = {}
    params["id"]=id;
    for (key of keys) {
            if(key !== "ID"){
                params[key.toLowerCase()] = $("#" + key + "_" + id).val()
            }
    }
    fetch("http://127.0.0.1:5000/edit-" + selectedTable, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify(params)
    })
}
