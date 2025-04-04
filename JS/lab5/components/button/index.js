export class ButtonComponent {
    constructor(parent) {
        this.parent = parent;
    }
    getHTML(data) {
        return (
            `<button type="button" class="btn btn-primary" data-id="${data[0]}" id="${data[0]}">${data[1]}</button>`
        )
    }
    
    addListeners(data, listener) {
        document
            .getElementById(`${data[0]}`)
            .addEventListener("click", listener)
    }
    
    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
    
}