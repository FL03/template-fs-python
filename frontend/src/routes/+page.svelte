<script>
    /** @type {import('./$types').PageData} */
    export let data;
    function handleCredentialResponse(response) {
        console.log("Encoded JWT ID token: " + response.credential);
    }
		
		
    async function handleClick () {
        google.accounts.id.initialize({
            client_id: process.env.CLIENT_ID,
            callback: handleCredentialResponse
        });
        google.accounts.id.renderButton(
        document.getElementById("loginBtn"),
        { theme: "outline", size: "large" }  // customization attributes
        );
        google.accounts.id.prompt(); // also display the One Tap dialog
    }
</script>

<svelte:head>
	<title>{data.head.title}</title>
	<meta name="description" content="{data.head.description}" />
</svelte:head>


<div class="flex flex-auto items-center justify-center rounded">
    <span class="prose text-center text-white">
        Welcome
    </span>
</div>

<form class="flex flex-auto flex-col min-h-full rounded-lg">
    <input autocomplete=""/>
     <!-- <button
        class="overflow-x-hidden py-1 px-2 inline-block mx-auto px-3 py-1 rounded items-center justify-center bg-gradient-to-r from-cyan-700 via-cyan-500 to-cyan-900 text-white max-w-24"
        id="loginBtn"
        on:click={handleClick}
        >
        Test
    </button> -->
</form>