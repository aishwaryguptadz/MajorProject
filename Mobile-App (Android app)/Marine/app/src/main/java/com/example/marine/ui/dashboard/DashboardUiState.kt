package com.example.marine.ui.dashboard

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.marine.ui.theme.MarineTheme

@Composable
fun DashboardStatsRow(viewModel: DashboardViewModel = viewModel()) {

    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceBetween
    ) {

        DashboardStatCard(
            title = "Total Ships",
            value = viewModel.shipCount.toString()
        )

        DashboardStatCard(
            title = "Active Ships",
            value = viewModel.activeShips.toString()
        )

        DashboardStatCard(
            title = "Alerts",
            value = viewModel.activeAlerts.toString()
        )
    }
}

@Composable
fun DashboardStatCard(
    title: String,
    value: String
) {

    Card(
        modifier = Modifier
            .width(110.dp)
            .height(90.dp)
            .background(MaterialTheme.colorScheme.surface),
        elevation = CardDefaults.cardElevation(6.dp)
    ) {

        Column(
            modifier = Modifier
                .background(MaterialTheme.colorScheme.surface)
                .fillMaxSize()
                .padding(12.dp),
            verticalArrangement = Arrangement.Center
        ) {

            Text(
                text = title,
                style = MaterialTheme.typography.bodySmall
            )

            Spacer(modifier = Modifier.height(4.dp))

            Text(
                text = value,
                style = MaterialTheme.typography.headlineSmall
            )
        }
    }
}

@Composable
fun FuelEfficiencySection() {

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .height(180.dp)
            .background(MaterialTheme.colorScheme.surface)
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(
                text = "Fuel Efficiency",
                style = MaterialTheme.typography.titleMedium
            )

            Spacer(modifier = Modifier.height(12.dp))

            Box(
                modifier = Modifier
                    .fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                Text("Fuel efficiency chart here")
            }
        }
    }
}

@Composable
fun SystemHealthRow() {

    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceBetween
    ) {

        HealthCard("Engine Health", "Good")
        HealthCard("Weather Risk", "Low")
    }
}

@Composable
fun HealthCard(title: String, status: String) {

    Card(
        modifier = Modifier
            .width(170.dp)
            .height(100.dp)
            .background(MaterialTheme.colorScheme.surface)
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(title)

            Spacer(modifier = Modifier.height(6.dp))

            Text(
                text = status,
                style = MaterialTheme.typography.headlineSmall
            )
        }
    }
}

@Composable
fun AlertsSection() {

    Card(
        modifier = Modifier
            .fillMaxWidth()
            .background(MaterialTheme.colorScheme.surface)
    ) {

        Column(
            modifier = Modifier.padding(16.dp)
        ) {

            Text(
                text = "Recent Alerts",
                style = MaterialTheme.typography.titleMedium
            )

            Spacer(modifier = Modifier.height(10.dp))

            Text("⚠ Engine anomaly detected")
            Text("⚠ Fuel efficiency drop detected")
            Text("⚠ Weather warning")
        }
    }
}

//
//@Preview(showBackground = true)
//@Composable
//fun DashboardCardPreview() {
//    MarineTheme {}
//}
