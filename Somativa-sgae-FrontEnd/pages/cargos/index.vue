<!-- CARGOS -->

<script setup>
    const { data: cargosReceived } = await useFetch('http://127.0.0.1:8000/cargos/',{
      key: 'cargosRequest'    
    });

    let showForm = false;
    const setShowForm = () => {
        //alert("Cliquei no botão!")
        showForm = true;
        refreshNuxtData()
    }   

    let name;

//função chamada quando o usuario clicar para enviar o formulario

const saveCargo = async() => {
   //imprimindo no console do navegador APENAS PARA TESTE
   console.log("nome", name);

   await useFetch('http://localhost:8000/cargos/',{
       method: 'POST',
   body:
   [{

       nome: name  
         
   }], onResponse(){
           alert("cargo saved");
           refreshNuxtData('cargosRequest')
       }
  
   
    });
}



</script>


<template>
    <div>
        <h1>
            Bem vindo aos Cargos
        </h1>
        
        <section v-for="cargo in cargosReceived.data" :key="cargo.id">
            
            <h3>{{ cargo.id}} - Nome: {{ cargo.nome }}</h3>
            
            

        </section>
        <hr>
        <br>
        <label for="add">Adicionar cargo? </label>
   
   <button @click="setShowForm">SIM</button>

    <!-- Elemento para exibir a descrição -->
    <section v-if="showForm === true">
        <br>
        <label for="">Nome do cargo: </label> <input type="text" v-model="name"> <br><br>
        <button @click="saveCargo">Salvar cargo</button>
    </section>
  

    <br>
    <br>
    
    <!-- <h2 v-if="detalhe !== ''" @click="realizarAcao">Login</h2> -->
    
    
        <hr>
    </div>

</template>


