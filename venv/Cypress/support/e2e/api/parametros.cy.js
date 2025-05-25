// cypress/e2e/api/parametros.cy.js

describe("API - /api/parametros (POST)", () => {
  it("deve adicionar parâmetro com sucesso", () => {
    const body = {
      lote: 1,
      temperatura: 25.5,
      umidade: 60.2,
      pressao: 1013.25,
      luminosidade: 800,
    };
    cy.request("POST", "/api/parametros", body).then((res) => {
      expect(res.status).to.eq(201);
      expect(res.body.parametro).to.have.property("id");
    });
  });

  it("deve retornar erro por campos faltando", () => {
    cy.request({
      method: "POST",
      url: "/api/parametros",
      body: { lote: 1 },
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(400);
      expect(res.body).to.have.property("campos_faltantes");
    });
  });

  it("deve retornar erro por tipo inválido", () => {
    const body = {
      lote: "abc",
      temperatura: "x",
      umidade: "x",
      pressao: "x",
      luminosidade: "x",
    };
    cy.request({
      method: "POST",
      url: "/api/parametros",
      body,
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(400);
      expect(res.body.error).to.include("Valores inválidos");
    });
  });
});

describe("API - /api/parametros (GET)", () => {
  it("deve retornar lista de parâmetros", () => {
    cy.request("/api/parametros").then((res) => {
      expect(res.status).to.eq(200);
      expect(res.body.data).to.be.an("array");
    });
  });
});

describe("API - /api/parametros/:id (PUT)", () => {
  it("deve atualizar parâmetro existente", () => {
    const body = {
      lote: 99,
      temperatura: 22,
      umidade: 55,
      pressao: 1000,
      luminosidade: 900,
    };
    cy.request("POST", "/api/parametros", body).then((res) => {
      const id = res.body.parametro.id;
      cy.request("PUT", `/api/parametros/${id}`, { lote: 100 }).then(
        (putRes) => {
          expect(putRes.status).to.eq(200);
          expect(putRes.body.parametro.lote).to.eq(100);
        }
      );
    });
  });

  it("deve retornar 404 para parâmetro inexistente", () => {
    cy.request({
      method: "PUT",
      url: "/api/parametros/999999",
      body: { lote: 123 },
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(404);
    });
  });
});

describe("API - /api/parametros/:id (DELETE)", () => {
  it("deve deletar parâmetro existente", () => {
    const body = {
      lote: 55,
      temperatura: 22.5,
      umidade: 44,
      pressao: 1011,
      luminosidade: 777,
    };
    cy.request("POST", "/api/parametros", body).then((res) => {
      const id = res.body.parametro.id;
      cy.request("DELETE", `/api/parametros/${id}`).then((delRes) => {
        expect(delRes.status).to.eq(200);
      });
    });
  });

  it("deve retornar 404 ao deletar parâmetro inexistente", () => {
    cy.request({
      method: "DELETE",
      url: "/api/parametros/999999",
      failOnStatusCode: false,
    }).then((res) => {
      expect(res.status).to.eq(404);
    });
  });
});
