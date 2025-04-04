// components/inner-page/index.js

import { BackButtonComponent } from "../../components/back-button/index.js";
import { MainPage } from "../../pages/main/index.js";

export class InnerPage {
    constructor(parent) {
        this.parent = parent;
    }

    // HTML для страницы
    getHTML(data) {
        return `
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="${data.photo_400_orig}" class="img-fluid" alt="картинка">
                        </div>
                    </div>
            `;
    }

    // Рендер страницы
    render(item) {
        const html = this.getHTML(item);
        this.parent.innerHTML = html;
        const backButton = new BackButtonComponent(this.parent);
        backButton.render(this.clickBack.bind(this));
    }

    clickBack() {
        const mainPage = new MainPage(this.parent);
        mainPage.render();
    }
}
