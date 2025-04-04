export class SortSelect {

    constructor(parent) {
        this.parent = parent;
    }


    // <option value="time_asc">В хронологическом порядке по вступлению в сообщество</option>
    // <option value="time_desc">В антихронологическом порядке по вступлению в сообщество</option>

    getHTML() {
        return (
            `
            <select id="sort-select" class="form-select" aria-label="Default select example">
                <option selected="selected" value="id_asc">В порядке возрастания ID</option>
                <option value="id_desc">В порядке убывания ID</option>
                <option value="time_asc">В хронологическом порядке по вступлению в сообщество</option>
                <option value="time_desc">В антихронологическом порядке по вступлению в сообщество</option>
            </select>
            `
        )
    }
    
    addListeners(listener) {
        const element = document.getElementById('sort-select')
        element.onchange = () => listener(element.value)
    }
    
    render(listener) {
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(listener)
    }
}