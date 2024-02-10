<script setup>
// função useFetch vai chamar o backend como se fosse no Insomnia
    const { data: allAmbientes } = await useFetch('http://localhost:8000/ambientes',{
      key: 'ambienteRequest' 
    });
    let showForm = false;
    const setShowForm = () => {
        //alert("Cliquei no botão!")
        showForm = true;
        refreshNuxtData()
    }   

    //criando as variáveis que vão armazenar os dados do formulario html
    let name;

     //função chamada quando o usuario clicar para enviar o formulario

     const saveAmbiente = async() => {
        //imprimindo no console do navegador APENAS PARA TESTE
        console.log("nome", name);

        await useFetch('http://localhost:8000/ambientes/',{
            method: 'POST',
        body:
        [{

		    nome: name  
              
        }], onResponse(){
                alert("ambiente saved");
                refreshNuxtData('ambienteRequest')
            }
       
        
         });
     }


</script>


<template>
    <div>
        <h1>
            Bem vindo aos ambientes
        </h1>
        
        <section v-for="ambiente in allAmbientes.data" :key="ambiente.id">
            
            <h3>{{ ambiente.id}} - Nome: {{ ambiente.nome }}</h3>
            

        </section>
        <hr>
        <label for="add">Adicionar ambiente? </label>
   
   <button @click="setShowForm">SIM</button>

    <!-- Elemento para exibir a descrição -->
    <section v-if="showForm === true">
        <br>
        <label for="">nome do ambiente: </label> <input type="text" v-model="name"> <br><br>
        <button @click="saveAmbiente">Salvar ambiente</button>
    </section>
  

    <br>
    <br>
    
    <!-- <h2 v-if="detalhe !== ''" @click="realizarAcao">Login</h2> -->
    
    
        <hr>
    </div>

</template>

