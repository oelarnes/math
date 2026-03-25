vim.api.nvim_create_autocmd({"BufEnter"}, {
    pattern = {"*.md"},
    callback = function()
        vim.keymap.set("n", "<leader>mm", "o```{math}<CR>:enumerated: false<CR><CR>```<ESC>O", { silent = true, buffer = true })
        vim.keymap.set("n", "<leader>md", "i$$<ESC>i", { silent = true, buffer = true })
    end
})
