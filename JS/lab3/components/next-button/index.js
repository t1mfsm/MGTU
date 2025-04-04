export class NextButtonComponent {
    constructor(parent) {
        this.parent = parent;
    }

    addListeners(listener) {
        document.getElementById("next-button").addEventListener("click", listener);
    }

    getHTML() {
        return `
            <button id="next-button" class="btn btn-primary" type="button">Вперед</button>
        `;
    }

    render(listener) {
        const html = this.getHTML();
        this.parent.insertAdjacentHTML('beforeend', html);
        this.addListeners(listener);
    }
}
