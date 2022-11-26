<script>
    import { Card, CardBody, Section } from '$lib';
    /** @type {import('./$types').PageData} */
    export let data;
    let card = {
        bg: "bg-zinc-500",
        color: 'text-white'
    }
</script>

<svelte:head>
	<title>{data.head.title}</title>
	<meta name="description" content="{data.head.description}" />
</svelte:head>


<div class="flex flex-auto items-center justify-between py-24 min-h-full max-h-screen min-w-full max-w-screen">
    <Section bg={"bg-transparent"}>
        <Card bg={card.bg} color={card.color} pd={"p-3"} props={""}>
            <CardBody>
                <span class="prose text-center">
                    Welcome to Proton
                </span>
            </CardBody>
        </Card>
    </Section>
</div>
