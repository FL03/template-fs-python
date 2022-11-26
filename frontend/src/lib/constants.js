export let info = {
    homepage: "/",
    metadata: {
        github: "scattered-systems",
        twitter: "scsys_eth"
    },
    name: "Proton",
    slug: "proton",
    sitemap: {
        href: "/",
        label: "Home",
        data: [
            {
                layout: "dashboard",
                label: "Dashboard",
                data: []
            }
        ]
    },
}

export let colors = {
    gradients: {
        cyan: ["bg-gradient-to-r from-cyan-700 via-cyan-500 to-cyan-900 text-white"]
    }
}

export let theme = {
    secondary: colors.gradients.cyan[0],
    button: {
        primary: "flex flex-initial px-3 py-1 rounded items-center justify-center"
    },
    link: "flex flex-initial overflow-y-clip hover:underline px-3 py-2 hover:opacity-75 text-white"
}