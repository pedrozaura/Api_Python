// cypress/e2e/api/itens.cy.js

describe("API - /api/data/itens (POST)", () => {
  it("deve criar um novo item com sucesso", () => {
    cy.request("POST", "/api/data/itens", { name: "Item de Teste" }).then(
      (res) => {
        expect(res.status).to.eq(201);
        expect(res.body).to.have.property("item");
        expect(res.body.item.name).to.eq("Item de Teste");
      }
    );
  });

  it("deve retornar erro 400 ao enviar dados inválidos", () => {
    cy.request({
      method: "POST",
      url: "/api/data/itens",
      body: {},
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(400);
      expect(res.body).to.have.property("error");
    });
  });
});

describe("API - /api/data (GET)", () => {
  it("deve retornar todos os itens com sucesso", () => {
    cy.request("/api/data").then((res) => {
      expect(res.status).to.eq(200);
      expect(res.body.data).to.be.an("array");
    });
  });
});

describe("API - /api/data/:id (PUT)", () => {
  it("deve atualizar um item existente", () => {
    cy.request("POST", "/api/data/itens", { name: "Item Atualizar" }).then(
      (res) => {
        const id = res.body.item.id;
        cy.request("PUT", `/api/data/${id}`, { name: "Item Atualizado" }).then(
          (updateRes) => {
            expect(updateRes.status).to.eq(200);
            expect(updateRes.body.item.name).to.eq("Item Atualizado");
          }
        );
      }
    );
  });

  it("deve retornar 404 para item inexistente", () => {
    cy.request({
      method: "PUT",
      url: "/api/data/999999",
      body: { name: "Teste" },
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(404);
    });
  });
});

describe("API - /api/data/delete/:id (DELETE)", () => {
  it("deve deletar um item existente", () => {
    cy.request("POST", "/api/data/itens", { name: "Item Delete" }).then(
      (res) => {
        const id = res.body.item.id;
        cy.request("DELETE", `/api/data/delete/${id}`).then((deleteRes) => {
          expect(deleteRes.status).to.eq(200);
        });
      }
    );
  });

  it("deve retornar 404 ao tentar deletar item inexistente", () => {
    cy.request({
      method: "DELETE",
      url: "/api/data/delete/999999",
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(404);
    });
  });
});
