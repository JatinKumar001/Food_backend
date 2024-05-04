import express from 'express'
import cors from 'cors'
import predictionRouter from './routes/prediction-router.js'
import recommendationRouter from './routes/recommendation-router.js'

const app = express();

app.use(cors())
app.use(express.json())

app.use("/api/prediction", predictionRouter)
app.use("/api/recommendation", recommendationRouter)

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("connected to backend");
})