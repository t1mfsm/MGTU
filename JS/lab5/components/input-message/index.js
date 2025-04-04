export class InputComponent {
    constructor(parent) {
        this.parent = parent;
    }
    getHTML() {
        return (
            `<div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="message" aria-label="Recipient's username" aria-describedby="basic-addon2" id="message">
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button" id="post">Button</button>
            </div>
          </div>`
        )
    }

    addListeners(listener) {
        document
            .getElementById(`post`)
            .addEventListener("click", listener)
    }

    render(listener) {
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(listener)
    }
    
}