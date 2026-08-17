package com.example.marine.ui.predictions

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MapsScreen(
    viewModel: PredictionsViewModel = viewModel()
) {

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {

        item {
            Text(
                text = "AI Predictions",
                style = MaterialTheme.typography.headlineMedium
            )

            Spacer(modifier = Modifier.height(16.dp))
        }

        item {
            PredictionCard(
                title = "Fuel Consumption Prediction",
                value = "${viewModel.predictedFuel} tons/day"
            )
        }

        item {
            PredictionCard(
                title = "Engine Failure Risk",
                value = "${viewModel.failureRisk}%"
            )
        }

        item {
            PredictionCard(
                title = "Anomaly Probability",
                value = "${viewModel.anomalyProbability}%"
            )
        }

        item {
            Spacer(modifier = Modifier.height(20.dp))
            PredictionGraphSection()
        }
    }
}

@Composable
fun PredictionGraphSection() {

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .height(200.dp)
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(
                text = "Prediction Trends",
                style = MaterialTheme.typography.titleMedium
            )

            Spacer(modifier = Modifier.height(12.dp))

            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                Text("Prediction graph will appear here")
            }
        }
    }
}

@Preview
@Composable
fun PreviewMapsScreen() {
    MapsScreen()
}