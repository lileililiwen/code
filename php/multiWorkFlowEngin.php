<?php

interface WorkflowEngine
{
    public function startWorkflow($workflowName, $input);
    public function getWorkflowStatus($workflowId);
    public function getWorkflowResult($workflowId);
}
class SimpleWorkflowEngine implements WorkflowEngine
{
    public function startWorkflow($workflowName, $input)
    {
        // 实现SimpleWorkflowEngine的startWorkflow方法
    }

    public function getWorkflowStatus($workflowId)
    {
        // 实现SimpleWorkflowEngine的getWorkflowStatus方法
    }

    public function getWorkflowResult($workflowId)
    {
        // 实现SimpleWorkflowEngine的getWorkflowResult方法
    }
}

class AdvancedWorkflowEngine implements WorkflowEngine
{
    public function startWorkflow($workflowName, $input)
    {
        // 实现AdvancedWorkflowEngine的startWorkflow方法
    }

    public function getWorkflowStatus($workflowId)
    {
        // 实现AdvancedWorkflowEngine的getWorkflowStatus方法
    }

    public function getWorkflowResult($workflowId)
    {
        // 实现AdvancedWorkflowEngine的getWorkflowResult方法
    }
}
class WorkflowEngineFactory
{
    public static function create($engineName)
    {
        switch ($engineName) {
            case 'simple':
                return new SimpleWorkflowEngine();
            case 'advanced':
                return new AdvancedWorkflowEngine();
            // 可以根据需要添加更多的工作流引擎
            default:
                throw new InvalidArgumentException('Invalid workflow engine name: ' . $engineName);
        }
    }
}
class AggregatedWorkflowEngine implements WorkflowEngine
{
    private $workflowEngine;

    public function __construct($engineName)
    {
        $this->workflowEngine = WorkflowEngineFactory::create($engineName);
    }

    public function startWorkflow($workflowName, $input)
    {
        return $this->workflowEngine->startWorkflow($workflowName, $input);
    }

    public function getWorkflowStatus($workflowId)
    {
        return $this->workflowEngine->getWorkflowStatus($workflowId);
    }

    public function getWorkflowResult($workflowId)
    {
        return $this->workflowEngine->getWorkflowResult($workflowId);
    }
}

$workflowEngine = new AggregatedWorkflowEngine('simple');
$workflowEngine->startWorkflow('workflow1', $input);
// ...

$workflowEngine = new AggregatedWorkflowEngine('advanced');
$workflowEngine->startWorkflow('workflow2', $input);
?>