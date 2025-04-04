import { PostComponent } from "../../components/post/index.js";
import { ajax } from "../../modules/ajax.js";
import { urls } from "../../modules/urls.js";
import { ID } from "../../modules/consts.js";

export class MainPage {
    constructor(parent) {
        this.parent = parent;
    }

    getData() {
        ajax.post(urls.getWallPosts(ID), (data) => {
            if (data.error) {
                console.error("Error fetching data:", data.error);
                this.showError("Error fetching data.");
                return;
            }
            this.renderData(data.response.items);
        });
    }

    renderData(posts) {
        posts.forEach((post) => {
            const postComponent = new PostComponent(this.pageRoot);
            postComponent.render(post);
        });
    }

    get pageRoot() {
        return document.getElementById("main-page");
    }

    getHTML() {
        return `
            <div id="main-page" class="d-flex flex-wrap"></div>
        `;
    }

    showError(message) {
        this.parent.innerHTML = `<div class="alert alert-danger" role="alert">${message}</div>`;
    }

    render() {
        this.parent.innerHTML = "";
        const html = this.getHTML();
        this.parent.insertAdjacentHTML("beforeend", html);

        this.getData();
    }
}
