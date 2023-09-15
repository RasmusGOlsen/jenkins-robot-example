pipeline {
    agent any
    triggers { pollSCM "H 20 * * *" }
    options {
        disableConcurrentBuilds()
        buildDiscarder logRotator(artifactNumToKeepStr: '10')
    }
    parameters {
        booleanParam(
            name: 'RunLint',
            defaultValue: true,
            description: 'Run the Lint stage when selected.')
        booleanParam(
            name: 'RunSimulation',
            defaultValue: true,
            description: 'Run the simulatiom stage when selected.')
        booleanParam(
            name: 'RunImplementation',
            defaultValue: true,
            description: 'Run the implementation stage when selected.')
    }
    environment {
        BUILDDIR = "_build"
        RUN_SH = "bin/robot.sh"
    }
    stages {
        stage(' ') {
            parallel {
                stage('lint') {
                    when { expression { params.RunLint == true }}
                    environment {
                        BUILDDIR = "${BUILDDIR}/${STAGE_NAME}"
                    }
                    steps {
                        sh "${RUN_SH} -i ${STAGE_NAME}"
                    }
                }
                stage('simulation') {
                    when { expression { params.RunSimulation == true }}
                    environment {
                        BUILDDIR = "${BUILDDIR}/${STAGE_NAME}"
                    }
                    steps {
                        sh "${RUN_SH} -i ${STAGE_NAME}"
                    }
                }
                stage('implementation') {
                    when { expression { params.RunImplementation == true }}
                    environment {
                        BUILDDIR = "${BUILDDIR}/${STAGE_NAME}"
                    }
                    steps {
                        sh "${RUN_SH} -i ${STAGE_NAME}"
                    }
                }
            }
        }
        stage('deploy') {
            when { expression { params.RunImplementation == true }}
            environment {
                BUILDDIR = "${BUILDDIR}/${STAGE_NAME}"
            }
            steps {
                sh "${RUN_SH} -i ${STAGE_NAME}"
            }
            post {
                success {
                    archiveArtifacts artifacts: "${BUILDDIR}/*.tar.gz"
                }
            }
        }
    }
    post {
        always {
            sh """
                rebot --nostatusrc --splitlog --merge -output output.xml -x xunit.xml --outputdir ${BUILDDIR} ${BUILDDIR}/*/output.xml
            """
            robot archiveDirName: 'robot-plugin', outputPath: "${BUILDDIR}"
            junit "${BUILDDIR}/xunit.xml"
        }
        unsuccessful {
            sh("test -d ${BUILDDIR} && tar -cf debug.tar.gz ${BUILDDIR}")
            archiveArtifacts artifacts: "debug.tar.gz"
        }
    }
}
