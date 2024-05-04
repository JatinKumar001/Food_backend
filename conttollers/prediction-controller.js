import { spawn } from "child_process"

let fooddata;
let ingredients1;
let ingredients2;
let ingredients3;
let ingredients4;
let ingredients5;
let ingredients6;

export const updateingredients = (req, res) => {

    const { ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6 } = req.body;

    ingredients1 = ingredient1
    ingredients2 = ingredient2
    ingredients3 = ingredient3
    ingredients4 = ingredient4
    ingredients5 = ingredient5
    ingredients6 = ingredient6

    res.json({ message: 'Ingredients updated successfully' });
}

export const getfoodprediction = (req, res) => {

    const childPython = spawn('python', ['foodprediction.py', ingredients1, ingredients2, ingredients3, ingredients4, ingredients5, ingredients6]);

    childPython.stdout.on('data', (data) => {
        // console.log(`${data}`);
        try {
            // const food_data = data;
            // res.status(200).json(`${data}`);
            fooddata = data
            res.send(data);
        }
        catch (err) {
            res.status(500).json(err);
        }
    })
}