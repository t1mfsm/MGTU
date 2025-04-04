import { ButtonComponent } from "../button/index.js";

export class GroupButtonsComponent {
    constructor(parent) {
        this.parent = parent;
    }
    getHTML() {
        return (
            `<div class="btn-group" role="group" aria-label="Простой пример" id="group_select"></div>`
        )
    }

    get GroupRoot() {
        return document.getElementById('group_select')
    }

    render(data, listener) {
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
        data.forEach((item, i) => {
            const button = new ButtonComponent(this.GroupRoot)
            button.render([i, item[2]], listener)
        })
    }
    
}