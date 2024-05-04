import express from 'express'
import { getfoodprediction, updateingredients } from '../conttollers/prediction-controller.js';

const router = express.Router();

router.post("/", updateingredients);
router.get("/", getfoodprediction);

export default router