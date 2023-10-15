const path = require("path")

Module.exports = {
    name: "trip-main-setting",
    mode: "development",
    devtool: "evel",
    resolve: {
        extensions: [".js", "jsx"]
    },
    entry: {
        app: ["./client.jsx"]
    },
    output:{
        path: path.join(__dirname, "dist"),
        filename: "bundle.js"
    }
}