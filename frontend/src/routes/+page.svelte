<script>
    /** @type {import('./$types').PageData} */
    export let data;
</script>

<svelte:head>
	<title>{data.head.title}</title>
	<meta name="description" content="{data.head.description}" />
</svelte:head>


<div class="flex flex-auto items-center justify-center rounded">
    <span class="prose text-center text-white">
        <h1 class="text-2xl prose text-white">Puzzled</h1>
        
    </span>
</div>