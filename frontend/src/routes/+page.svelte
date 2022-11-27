<script>
    /** @type {import('./$types').PageData} */
    export let data;
    import abstractShapes from '$lib/assets/media/abstractShapes.svg';
</script>

<svelte:head>
	<title>{data.head.title}</title>
	<meta name="description" content="{data.head.description}" />
</svelte:head>


<div class="flex flex-auto items-center justify-center rounded">
    <div class="rounded flex"><img alt="#" src="{abstractShapes}" class="flex "/></div>
    <span class="prose text-center text-white">
        Welcome
    </span>
</div>
