describe("API Embriotec - Testes de CRUD", () => {
  const baseUrl = "http://localhost:5000"; // ajuste se necessário

  // ---------- TESTES COM ITEM ----------
  it("Cria um novo item", () => {
    cy.api({
      method: "POST",
      url: `${baseUrl}/api/data/itens`,
      body: {
        name: "Item de Teste",
      },
    }).then((res) => {
      expect(res.status).to.eq(201);
      expect(res.body).to.have.property("item");
      cy.wrap(res.body.item.id).as("itemId");
    });
  });

  it("Recupera todos os itens", () => {
    cy.api(`${baseUrl}/api/data`).then((res) => {
      expect(res.status).to.eq(200);
      expect(res.body.data).to.be.an("array");
    });
  });

  it("Atualiza um item", function () {
    const updatedName = "Item Atualizado";
    cy.api("POST", `${baseUrl}/api/data/itens`, { name: "Para Atualizar" })
      .its("body.item.id")
      .then((id) => {
        cy.api("PUT", `${baseUrl}/api/data/${id}`, { name: updatedName }).then(
          (res) => {
            expect(res.status).to.eq(200);
            expect(res.body.item.name).to.eq(updatedName);
          }
        );
      });
  });

  it("Deleta um item", () => {
    cy.api("POST", `${baseUrl}/api/data/itens`, { name: "Para Deletar" })
      .its("body.item.id")
      .then((id) => {
        cy.api("DELETE", `${baseUrl}/api/data/delete/${id}`).then((res) => {
          expect(res.status).to.eq(200);
        });
      });
  });

  // ---------- TESTES COM PARAMETRO ----------
  it("Cria um novo parâmetro", () => {
    const body = {
      lote: 101,
      temperatura: 24.5,
      umidade: 55.3,
      pressao: 1013.25,
      luminosidade: 500,
    };
    cy.api("POST", `${baseUrl}/api/parametros`, body).then((res) => {
      expect(res.status).to.eq(201);
      expect(res.body.parametro).to.include(body);
    });
  });

  it("Lista todos os parâmetros", () => {
    cy.api("GET", `${baseUrl}/api/parametros`).then((res) => {
      expect(res.status).to.eq(200);
      expect(res.body.data).to.be.an("array");
    });
  });

  it("Atualiza um parâmetro", () => {
    const body = {
      lote: 202,
      temperatura: 23.1,
      umidade: 60,
      pressao: 1012,
      luminosidade: 450,
    };
    cy.api("POST", `${baseUrl}/api/parametros`, body)
      .its("body.parametro.id")
      .then((id) => {
        cy.api("PUT", `${baseUrl}/api/parametros/${id}`, {
          temperatura: 26.0,
          umidade: 65.0,
        }).then((res) => {
          expect(res.status).to.eq(200);
          expect(res.body.parametro.lote).to.eq(body.lote);
        });
      });
  });

  it("Deleta um parâmetro", () => {
    cy.api("POST", `${baseUrl}/api/parametros`, {
      lote: 303,
      temperatura: 20,
      umidade: 50,
      pressao: 1011,
      luminosidade: 400,
    })
      .its("body.parametro.id")
      .then((id) => {
        cy.api("DELETE", `${baseUrl}/api/parametros/${id}`).then((res) => {
          expect(res.status).to.eq(200);
        });
      });
  });
});
