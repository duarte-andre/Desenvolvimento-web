<script setup>
  // acessamos o mecanismo de rotas do NUXT
  const route = useRoute();
  const { data: tarefaFound } = await useFetch(`http://localhost:8000/tarefas/${route.params.id}`, {
    key: 'tarefaRequest'
  });

  const { data: sttsFound } = await useFetch(`http://localhost:8000/tarefasStatus`, {
    key: 'tarefasttsRequest'
  });

  const { data: fotosFound } = await useFetch(`http://localhost:8000/fotos?tarefa=${route.params.id}`, {
    key: 'fotosRequest'
  });

  const paramsID = route.params.id;
</script>

<template>
  <div>
    <h1>Detalhes da Tarefa {{ tarefaFound.data.nome }}</h1>
    <br>
    <section>
      <h3>Status: {{ tarefaFound.data.idStatusFK.nome }}</h3>
      <h3>Ambiente: {{ tarefaFound.data.idAmbienteFK.nome }}</h3>
      <h3>Prazo: {{ tarefaFound.data.prazo }}</h3>
    </section>
    <section v-if="mostrar">
      <h3>Data de início: {{ tarefaFound.data.dataInicio }}</h3>
      <h3>Data término: {{ tarefaFound.data.dataFim }}</h3>
      <h3>Descrição: {{ tarefaFound.data.descricao }}</h3>
      <h3>Solicitante: {{ tarefaFound.data.idSolicitanteFK.nome }}</h3>
      <img :src="tarefaFound.data.idSolicitanteFK.image" alt="Imagem do solicitante">
      <p>Imagem do solicitante: {{ tarefaFound.data.idSolicitanteFK.nome }}</p>

      <h3>Histórico</h3>
      <section v-for="stts in sttsFound.data" :key="stts.id">
        <h4 v-if="stts.idTarefaFK == paramsID">Nome: {{ stts.idStatusFK.nome }} / Data: {{ stts.data }} / Descrição: {{ stts.descricao }}</h4>
      </section>

      <h3>Fotos da Tarefa</h3>
      <div v-for="foto in fotosFound.data" :key="foto.id">
        <h4>{{ foto.nome }}</h4>
        <img :src="foto.image" alt="Imagem da Tarefa">
      </div>
    </section>

    <br>
    <label v-if="!mostrar" for="Detalhes">Detalhes? </label>
    <button v-if="!mostrar" @click="exibirDescricao">SIM</button>
    <br>
    <br>

    <NuxtLink :to="`/tarefas`">
      <button>Voltar</button>
    </NuxtLink>
    <br>
    <hr>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mostrar: false // Variável para controlar a exibição da descrição
    };
  },
  methods: {
    exibirDescricao() {
      // Função para mostrar a descrição
      this.mostrar = true;
    }
  }
};
</script>
